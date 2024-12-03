class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f"{self.name} атаковал {other.name}")
        other.health -= self.attack_power
        print(f"У {other.name} осталось {other.health} здоровья")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} выиграл!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} выиграл!")
                break


# Создание экземпляров героев и начало игры
player = Hero("Человек", 100, 20)
computer = Hero("Компьютер", 100, 20)
game = Game(player, computer)
game.start()
Замени в этой программе  "if not "   на == или  !=  совместно с False или True