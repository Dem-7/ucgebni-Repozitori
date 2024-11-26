class Person:
    def __init__(self, name, age):
        self.name = name  # Инициализация атрибута name
        self.age = age    # Инициализация атрибута age
    def a (self):
        print("Привет мир")
# Создание экземпляра класса Person
person1 = Person("Alice", 30)

print(person1.name)  # Вывод: Alice
print(person1.age)
person1.a()



