import random
class Animals:
    live = True
    sound = None
    _DEGREE_OF_DENGER = 0  # Степень опасности

    def __init__(self, speed):
        self._cords = [0,0,0] # [0,0,0] координаты в пространстве
        self.speed = speed

       # super().__init__(speed)


    def move(self, dx, dy, dz):
        self._cords =[int(dx)*int(self.speed), int(dy)*int(self.speed), int(dz)*int(self.speed)]
        if self._cords[2] < 0:
            print(f" It's too deep, i can't dive :(")
            self._cords[2]=0


    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DENGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'mattacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animals):
    beak = True  # Наличие клюва

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f' Here are(is) {eggs_count} eggs for you')


class AquaticAnimal(Animals):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz_abs = abs(dz)
        new_z = self._cords[2] - (dz_abs / 2) * self.speed
        if new_z < 0:
            print("It's too deep, i csn't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animals):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"  # Звук утконоса
    _DEGREE_OF_DENGER = PoisonousAnimal._DEGREE_OF_DANGER

if __name__ == '__main__':
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    print(db._DEGREE_OF_DENGER)
    db.attack()

    db.move(1,2,3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()