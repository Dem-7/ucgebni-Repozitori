class Task ():
    def __init__(self, opisanie, srok, status):
        self.opisanie = opisanie
        self.srok = srok
        self.status = status
        self.spisok = []
        self.spisok1 = []
    def dobavlenie (self ,r):
        self.spisok.append( r)


    def vipolnen (self, r):
        print(f"Задача {r} выполнена")
        self.status  = "выполнено"
    def otmechanie (self):
        for a in self.spisok:
            if a == "выполнено":
                self.spisok1.append(a)




task = Task(1 , 2 ,3)
task.dobavlenie("Учиться")
task.dobavlenie("Поспать")
print(task.spisok)
task.vipolnen("Учиться")
