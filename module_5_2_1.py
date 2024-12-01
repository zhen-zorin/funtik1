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

    def isinst(self, other):
        if isinstance(other,int) and isinstance(self,int):
            return True
        elif isinstance(self,House) and isinstance(other,House):
            return True
        else:
            return print('Разные типы данных')

    def __eq__(self, other):# self, other -
        if self.isinst(other):
            if self.number_of_floor == other.number_of_floor :
                return True
            else:
                return False

    def __lt__(self, other):
        if self.isinst(other):
            if self.number_of_floor < other.number_of_floor :
                return True
            else:
                return False

    def __le__(self, other):
        if self.isinst(other):
            if self.number_of_floor <= other.number_of_floor :
                return True
            else:
                return False

    def __gt__(self, other):
        if self.isinst(other):
            if self.number_of_floor > other.number_of_floor :
                return True
            else:
                return False

    def __ge__(self, other):
        if self.isinst(other):
            if self.number_of_floor >= other.number_of_floor :
                return True
            else:
                return False

    def __ne__(self, other):
        if self.isinst(other):
            if self.number_of_floor != other.number_of_floor :
                return True
            else:
                return False
    def __add__(self, value):
        rez_floor = self.number_of_floor +value
        self.number_of_floor = rez_floor
        print(f'Название: {self.name}, кол-во этажей: {rez_floor}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(21)
h1.__str__()
h2.__str__()
print(h1.__eq__(h2))
h1.__add__(10)
print(h1.__eq__(h2))
h1.__add__(10)
h2.__add__(10)
print(h1.__gt__(h2))
print(h1.__ge__(h2))
print(h1.__lt__(h2))
print(h1.__le__(h2))
print(h1.__ne__(h2))


