import math


class Figure:
    sides_count = 0  # нужное  кол-во сторон

    def __init__(self,  color, *sides):
        self.filled = False # закрашеный
        self.__sides = [] # список сторон, целые числа
        self.__color = [] # список цветов в формате RGB

        if not (self.__is_valid_sides(*sides)):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

        if self.__is_valid_color(list(color)[0], list(color)[1], list(color)[-1]):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r, g, b): # r,g,b целые числа от 0 до 255
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b): # меняем список цветов
        if self.__is_valid_color(r,g,b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self): # периметр
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)

        if isinstance(circumference, (int, float)) and 0 < circumference :
            self.__radius = circumference / (2 * math.pi)
            self.set_sides(circumference)

    def get_square(self):
        return (self.__radius ** 2) * math.pi # площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self,color, a, b, c):
        super().__init__(color,a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        if all(isinstance(i, (int, float)) and 0 < i  for i in (a, b, c)):
            s = (a + b + c) / 2 # полупериметр
            return math.sqrt(s * (s - a) * (s - b) * (s - c))



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color)
        if  isinstance(edge_length, (int, float)):
            self.set_sides(*[edge_length] * self.sides_count)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3





circle1 = Circle((200, 200, 100), 10)
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