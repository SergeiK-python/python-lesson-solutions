# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"

# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first: str, second, third):
#         self.first = first
#         print(first)
#         print(second)
#         print(third)
#
#     def __del__(self):
#         print(f"{self.first} is deleting")
#         del self
#
#
# ex1 = Example('data1', second=25, third=3.14)
# ex2 = Example('data2', second={}, third=[])
# ex3 = Example('data3', second={}, third=[])
# ex4 = Example((), second={}, third=[])
# del ex1
# print("manual deleting done")


class House:
    houses_history = []

    def __new__(cls, name: str, *args, **kwargs):
        cls.houses_history.append(name)
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        del self

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return not self == other

    def __add__(self, value: int):
        self.number_of_floors += value
        return self

    def __radd__(self, value: int):
        return self + value

    def __iadd__(self, value: int):
        return self + value


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
