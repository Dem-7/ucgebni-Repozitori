
class Task:
    def __init__(self, opisanie, srok, status):
        self.opisanie = opisanie
        self.srok = srok
        self.status = status
        self.spisok = []  # Список задач
        self.spisok1 = []  # Список выполненных задач

    def dobavlenie(self, r):
        self.spisok.append({'opisanie': r, 'status': 'не выполнено'})  # Добавляем задачу как словарь

    def vipolnen(self, r):
        for a in self.spisok:

            if a['opisanie'] == r:
                a['status'] = 'выполнено'  # Изменяем статус задачи
                print(f"Задача {r} выполнена")


    def otmechanie(self):
        for a in self.spisok:
            if a['status'] != " выполнено":
                self.spisok1.append(a['opisanie'])  # Добавляем выполненные задачи в spisok1

task = Task(1, 2, 3)
task.dobavlenie("Учиться")
task.dobavlenie("Делать зарядку")
task.dobavlenie("Читать")
print(task.spisok)

task.vipolnen("Учиться")

task.otmechanie()  # Сохраняем выполненные задачи
print(task.spisok1)  # Выводим список выполненных задач
