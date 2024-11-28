
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Luk(Weapon):
    def attack(self):
        print("Боец выбирает лук")
        print( "Боец стреляет в монстра из лука")
        print( "Монстр повержен бойцом")

class Monster():
            pass


class Mech(Weapon):
    def attack(self):

        print("Боец выбирает меч ")
        print("Боец бъёт монстра мечём")
        print("Монстр повержен бойцом")


class Fighter():
    def __init__ (self, tt):
        self.tt = tt
    def change_weapon (self):
        self.tt.attack()

luk = Luk()
mech = Mech()
finger = Fighter(luk)
finger.change_weapon()
finger = Fighter(mech)
finger.change_weapon()


def nn (l):
    print(l)

nn(mech)






