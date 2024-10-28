import math

class Figure:
    sides_count = 0

    def __init__(self, *vhod):
        __vhod = list(vhod)
        self.color = __vhod.pop(0)
        self.sides = __vhod
        self.filled = False

    def get_color(self):
        return list(self.color)

    def __is_valid_color(self, r=0, g=0, b=0):
        if r < 0 or r > 255:
            return False
        elif g < 0 or g > 255:
            return False
        elif b < 0 or b > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = list(self.color)
            self.color[0] = r
            self.color[1] = g
            self.color[2] = b

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for i in new_sides:
            if i < 0 and (i * 10) % 10 != 0:
                return False
        else:
            return True

    def get_sides(self):
        return self.sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def __len__(self):
        return sum(self.sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, *vhod):
        super().__init__(*vhod)
        if len(self.sides) > 1:
            self.sides = 1
        elif (self.sides[0] * 10) % 10 != 0:
            self.sides = 1
        else:
            self.sides = self.sides[0]
        self.__radius = self.sides / 6.28

    def get_square(self):
        return (self.sides ** 2) / 12.56


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *vhod):
        super().__init__(*vhod)
        if len(self.sides) != 3:
            self.sides = [1, 1, 1]
        elif (self.sides[0] * 10) % 10 != 0:
            self.sides = [1, 1, 1]
        elif (self.sides[1] * 10) % 10 != 0:
            self.sides = [1, 1, 1]
        elif (self.sides[2] * 10) % 10 != 0:
            self.sides = [1, 1, 1]
        else:
            self.sides = list(self.sides)


    def get_square(self):
        return 0.25 * math.sqrt(4 * (self.sides[0] ** 2) * (self.sides[1] ** 2) -
                                ((self.sides[0] ** 2) + (self.sides[1] ** 2) - (self.sides[2] ** 2)) ** 2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, *vhod):
        super().__init__(*vhod)
        if len(self.sides) == 1 and (self.sides[0] * 10) % 10 == 0:
            side_of_the_cube = int(self.sides[0])
            self.sides = []
            for i in range(0, 12):
                self.sides.append(side_of_the_cube)
        else:
            self.sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_volume(self):
        return self.sides[0] ** 3


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