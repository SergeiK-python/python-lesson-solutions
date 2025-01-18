# Домашнее задание по теме "Написание примитивной ORM"

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from files.crud_functions import get_all_products, is_user_exists, add_user


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


api = "hahaha"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

products = get_all_products()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(KeyboardButton(text='Рассчитать'),
       KeyboardButton(text='Информация'),
       KeyboardButton(text='Купить'),
       KeyboardButton(text='Регистрация'))

kbA = InlineKeyboardMarkup(resize_keyboard=True)
kbA.row(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
       InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'))

kbB = InlineKeyboardMarkup(resize_keyboard=True)
kbB.row(InlineKeyboardButton(text='Product1', callback_data='product_buying'),
        InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        InlineKeyboardButton(text='Product3', callback_data='product_buying'),
        InlineKeyboardButton(text='Product4', callback_data='product_buying'))



@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_user_exists(message.text):
        # await state.finish()
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    username = data.get('username')
    add_user(username, data.get('email'), int(data.get('age')))
    await state.finish()
    if is_user_exists(username):
        await message.answer('Регистрация прошла успешно')
    else:
        await message.answer('Ошибка регистрации')

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1,5):
        with open(f'./files/productSB{i}.jpg', 'rb') as img:
            product = products[i]
            await message.answer(f"Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}")
            await message.answer_photo(img)
            # message.answer_photo(img, caption=f"Название: {product[0]} | Описание: описание {product[1]} | Цена: {product[2]}")
    await message.answer('Выберите продукт для покупки:', reply_markup=kbB)

@dp.callback_query_handler(lambda c: c.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


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
