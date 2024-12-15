from random import randrange
dd = randrange(1, 83, 3)
print(dd)
if dd % 2 == 0:
    print("Выбрано чётное число ")
else:
    print("Выбранное число нечётное")