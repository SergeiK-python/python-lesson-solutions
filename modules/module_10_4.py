from threading import Thread
from queue import Queue
import random
from time import sleep


class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

    def set_guest(self, guest):
        self.guest = guest

    def is_empty(self):
        return self.guest is None

    def clean(self):
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        sleep(wait_time)

class Cafe:
    def __init__(self, *args):
        self.tables = [*args]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self._get_free_table()
            if table is None:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
            else:
                self._lock_table(table, guest, "сел(-а) за стол номер")

    def discuss_guests(self):
        while not self.queue.empty():
            table = self._get_free_table()
            if not table is None:
                if self._is_table_closing(table):
                    self._clean_table(table)
                guest = self.queue.get()
                self._lock_table(table, guest, "вышел(-ла) из очереди и сел(-а) за стол номер")

        #print("Очередь пуста")
        table = self._get_locked_table()
        while not table is None:
            if self._is_table_closing(table):
                self._clean_table(table)
            sleep(1)
            table = self._get_locked_table()
        #print("Кафе свободно")

    def _clean_table(self, table):
        if not table.is_empty():
            print(f"Гость {table.guest.name} покушал(-а) и ушёл(ушла)")
            table.clean()
            print(f"Стол номер {table.number} свободен")

    def _lock_table(self, table, guest, string):
        table.set_guest(guest)
        table.guest.start()
        print(f"{table.guest.name} {string} {table.number}")

    def _get_free_table(self):
        for table in self.tables:
            if table.is_empty():
                return table
            elif self._is_table_closing(table):
                return table

        return None

    def _get_locked_table(self):
        for table in self.tables:
            if not table.is_empty():
                return table
        return None

    def _get_dirty_table(self):
        for table in self.tables:
            if self._is_table_closing(table):
                return table
        return None

    def _is_table_closing(self, table):
        return not (table.is_empty() or table.guest.is_alive())

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

#print("Кафе закрыто")
