# Дополнительное практическое задание по модулю*
from numpy import pi as PI, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color: tuple, sides: list):
        self._sides = sides
        self._color = [0, 0, 0]
        self.set_color(color[0], color[1], color[2])
        self.filled = False

    def get_color(self):
        return self._color

    def _is_valid_color(self, r: int, g: int, b: int) -> bool :
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r: int, g: int, b: int):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]


    def _is_valid_sides(self, *new_sides) -> bool :
        count = 0
        for arg in new_sides:
            if isinstance(arg, int) and arg > 0:
                count += 1
            else:
                break
        else:
            if count == len(self.get_sides()):
                return True
            else:
                return False

        return False

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *new_sides):
            super().__init__(color, [1] * Circle.sides_count)
            self.set_sides(*new_sides)
            self._radius = self.__len__() / 2.0 / PI

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self._radius = self.__len__() / 2.0 / PI

    def get_square(self):
        return PI * self._radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *new_sides):
            super().__init__(color, [1] * Triangle.sides_count)
            self.set_sides(*new_sides)

    def get_square(self):
        half_p = self.__len__() / 2
        return sqrt(half_p * (half_p - self._sides[0]) * (half_p - self._sides[1]) * (half_p - self._sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *new_sides):
        super().__init__(color, [1] * Cube.sides_count)
        new_sides = [*new_sides] * Cube.sides_count
        self.set_sides(*new_sides)

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

triangle1 = Triangle((200, 200, 100), 3, 5, 4)
#print(len(triangle1))
#print(triangle1.get_sides())
#print(triangle1.get_square())
#triangle1.set_sides(4, 3, 5)
#print(triangle1.get_sides())
#print(triangle1.get_square())

#circle1.set_sides(10)
#print(circle1.get_square())
#print(circle1._radius * 2 * PI)
#circle1.set_sides(100)
#print(circle1.get_square())
#print(circle1._radius * 2 * PI)
