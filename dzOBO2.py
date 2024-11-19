
class User():
    def __init__(self, id, imy, uroven):
        self._id = id
        self._imy = imy
        self._uroven = uroven
        self.spisok = []

class Admin(User):
    def __init__(self, id, imy, uroven):
        super().__init__(id, imy, uroven)
        self.__svoikabinet = "Свой кабинет"


    def __dobovlenie(self, element):
        self.spisok.append(element)

    def __udolenie(self, element):
        if element in self.spisok:
            self.spisok.remove(element)

    def otkrivalka(self , element ):
        self.__dobovlenie(element)
    def otkrivalka1(self,element):
        self.__udolenie(element)

admin = Admin(231, "Борис", 2)
admin.otkrivalka("Васильев")
admin.otkrivalka("Петров")
admin.otkrivalka("Кузнецов")
admin.otkrivalka("зеленцов")
admin.otkrivalka1("Петров")
print(admin.spisok)

