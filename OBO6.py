# Класс Hero:
#
# Атрибуты:
#
# Имя (name)
#
# Здоровье (health), начальное значение 100
#
# Сила удара (attack_power), начальное значение 20
#
# Методы:
#
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
#
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
#
# Класс Game:
#
# Атрибуты:
# Игрок (player), экземпляр класса Hero
#
# Компьютер (computer), экземпляр класса Hero
# Методы:
#
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.


class Hero():
     def __init__ (self , name ,health = 100 , attack_power = 20 ):
        self.name = name
        self.health = health
        self.attack_power = attack_power

     def attack(self , other):
        print(f" {self.name} атаковал {other.name} ")
        other.health -= self.attack_power
        print(f"У {other.name} осталось {other.health} здоровья  ")


     def is_alive (self):
         return self.health > 0

class Game():
    def __init__ (self, player , computer):
        self.player = player
        self.computer = computer

    def start(self):
        while True:
           self.player.attack(self.computer)
           if self.computer.is_alive () == False:
            print( f"{self.player.name} выиграл")
            break

           self.computer.attack(self.player)
           if self.player.is_alive() == False:
            print(f"{self.computer.name} выиграл")
            break

player = Hero("Человек" ,100 , 20 )
computer = Hero("Компьютер", 100, 20)
game = Game(player , computer)
game.start()







