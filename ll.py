# Нейрокот, [02.12.2024 21:50]
# Вот пример простой текстовой боевой игры с использованием ООП, где игрок и компьютер управляют героями.
# Игра состоит из раундов, в каждом из которых игроки по очереди атакуют друг друга,
# пока здоровье одного из героев не закончится.


import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        other.health -= damage
        print(f"{other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} выиграл!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} выиграл!")


# Создание экземпляров героев
player_name = input("Введите имя вашего героя: ")
player = Hero(player_name)
computer = Hero("Компьютер")

# Запуск игры
game = Game(player, computer)
game.start()


# ### Объяснение кода:
#
# 1. **Класс Hero**:
#    - Содержит атрибуты `name`, `health`, и `attack_power`.
#    - Метод `attack` принимает другого героя как аргумент и наносит ему урон.
#    - Метод `is_alive` проверяет, жив ли герой.
#
# 2. **Класс Game**:
#    - Содержит ссылки на игрока и компьютера.
#    - Метод `start` управляет игровым процессом, чередуя ходы между игроком и компьютером,
#    пока один из них не потеряет все здоровье.
#
# 3. **Создание экземпляров**:
#    - Пользователь вводит имя своего героя.
#    - Создается экземпляр компьютера с фиксированным именем "Компьютер".
#
# 4. **Запуск игры**:
#    - Игра начинается с вызова метода `start`.
#
# ### Запуск программы:
# Скопируйте и вставьте код в среду вып
#
# Нейрокот, [02.12.2024 21:50]
# олнения Python, чтобы начать игру. Игрок будет по очереди атаковать компьютера,
# пока один из них не победит.