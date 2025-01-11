# Домашнее задание по теме "Инлайн клавиатуры".

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = "hahaha"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация'))
kbA = InlineKeyboardMarkup(resize_keyboard=True)
kbA.row(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
       InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'))



@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kbA)

@dp.callback_query_handler(lambda c: c.data == 'formulas')
async def get_formulas(call):
    await call.message.answer('10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5')

@dp.callback_query_handler(lambda c: c.data == 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    #print(data.get('age'), data.get('growth'), data.get('weight'))
    calories = 10 * int(data.get('weight')) + 6.25 * int(data.get('growth')) - 5 * int(data.get('age')) + 5
    await message.answer(f'Норма ваших калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    #print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
