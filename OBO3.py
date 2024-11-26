


class Animal ():
    def __init__ (self, imy , vozrast):
        self.imy = imy
        self.vozrast = vozrast

    def make_sound(self):
        print("Голос животного")
    def  eat(self):
        print("Еда животного")
    def mm (self):
        print("Животные и сотрудники мирно сосуществуют в зоопарке")  #  Информация о животных
                                                                      #   и сотрудниках
class  Bird(Animal):
    def __init__ (self ,imy , vozrast, kluv ):
        super().__init__(imy , vozrast )
        self.kluv = kluv
    def make_sound(self):
        print("Щебетание")
class Mammal(Animal):
    def __init__ (self ,imy , vozrast, moloko ):
        super().__init__(imy , vozrast )
        self.moloko = moloko
    def make_sound(self):
        print("Рычание")
class Reptile(Animal):
    def __init__ (self ,imy , vozrast, xvost ):
        super().__init__(imy , vozrast )
        self.xvost = xvost
    def make_sound(self):
        print("Шипение")
bird = Bird("Страусы" , "3" , "большой")
mammal =Mammal("Собаки " , "8" , "Жирное")
reptile = Reptile("Змеи" , "5" , "Длиный")
animals =[bird , mammal , reptile]
def animal_sound(animals):# Полиморфизм
    for a in animals:
        a.make_sound()
animal_sound(animals)
class Zoo ():
    def __init__ (self):
        self.animal = Animal          # Композиция    строки 13 и 14  + 53, 54
        self.zivnost = []
        self.sotrudniki = []

    def a(self ,r):
        self.sotrudniki .append(r) # Добовляем сотрудников

    def b(self, r):
        self.zivnost.append(r) # Добовляем животных
    def ll (self):
        self.animal.mm(self)   # Вызываем метод mm у класса Animal
class ZooKeeper():
    def feed_animal(self):
        print(f"Сотрудники   кормят животных ")

zooKeeper = ZooKeeper()
zooKeeper.feed_animal()
class Veterinarian():
   def heal_animal(self):
       print(f"Ветиринары  лечит животных зоопарка ")
veterinarian = Veterinarian()
veterinarian.heal_animal()

zoo = Zoo()
zoo.ll()





