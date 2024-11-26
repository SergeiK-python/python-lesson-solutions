# Домашнее задание по теме "Потоки на классах"
import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        time_in = time.time()
        enemy = 100
        while enemy > 0:
            enemy -= self.power
            if enemy < 0:
                enemy = 0

            sleep(1)
            print(f'{self.name}, сражается {int(time.time() - time_in)} день(дня)..., осталось {enemy} воинов.\n')
        print(f'{self.name} одержал победу спустя {int(time.time() - time_in)} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")