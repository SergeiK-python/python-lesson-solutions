#  Домашнее задание по теме "Зачем нужно наследование"

class Unit:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Plant(Unit):
    def __init__(self, name: str, edible=False):
        super().__init__(name)
        self.edible = edible


class Animal(Unit):
    def __init__(self, name: str, alive=True, fed=False):
        super().__init__(name)
        self.alive = alive
        self.fed = fed

    def eat(self, food: Plant):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self} съел {food}")
            else:
                self.alive = False
                print(f"{self} не стал есть {food}")
        else:
            print(f"{self} не знает, что это такое {type(food)}")


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name, True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
