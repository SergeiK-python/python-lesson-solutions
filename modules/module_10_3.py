# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import random
from time import sleep

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        counter = 100
        while counter > 0:
            if self.balance >= 500 and lock.locked():
                lock.release()
            added = random.randint(50, 500)
            self.balance += added
            print(f"Пополнение: {added}. Баланс: {self.balance}")
            counter -= 1
            sleep(0.001)

    def take(self):
        counter = 100
        while counter > 0:
            taken = random.randint(50, 500)
            print(f"Запрос на {taken}")
            if self.balance >= taken:
                self.balance -= taken
                print(f"Снятие: {taken}. Баланс: {self.balance}")
                counter -= 1
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()


bk = Bank()

    # Так как методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
