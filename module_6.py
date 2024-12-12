class Animal:
    def __init__(self, name,):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name  # индевидуальное имя

    def eat(self, food):  # объекты классов растений
        if food.edible == True:  # съедобное
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    def __init__(self, name, edible=False):
        self.edible = False  # съедобность
        self.name = name  # индивидуальное название каждого растения


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.fed = False
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.fed = False
        self.name = name


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # съедобность
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


if __name__ == '__main__':
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
