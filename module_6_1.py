class Vehicle:
    __COLOR_VARIANS = ['red', 'black', 'green', 'white', 'blue']
    def __init__(self, owner, model, color, endine_power):
        self.owner = owner
        self.__model = model
        self.__endine_power = endine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__endine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f' {self.get_model()}\n {self.get_horsepower()}\n {self.get_color()}\n Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANS:
            self.__color = new_color
        else:
            return  print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # количество мест


if  __name__ == '__main__':
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изночальные методы
    vehicle1.print_info()

    # Меняем свойства( в т.ч. методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

