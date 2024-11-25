class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Такого этажа не существует')
        else:
            for floor in range(1,new_floor + 1):
                print(floor)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')

    def __len__(self ):
        print( self.number_of_floor)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(5)
h2.go_to(21)
h1.__str__()
h2.__str__()
h1.__len__()
h2.__len__()

