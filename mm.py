
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
        for task in self.spisok:
            if task['opisanie'] == r:
                task['status'] = 'выполнено'  # Изменяем статус задачи
                print(f"Задача {r} выполнена")
                return
        print(f"Задача {r} не найдена")  # Сообщение, если задача не найдена

    def otmechanie(self):
        for task in self.spisok:
            if task['status'] == "выполнено":
                self.spisok1.append(task['opisanie'])  # Добавляем выполненные задачи в spisok1

task = Task(1, 2, 3)
task.dobavlenie("Учиться")
task.dobavlenie("Поспать")
task.dobavlenie("Читать")
print(task.spisok)

task.vipolnen("Учиться")
task.otmechanie()  # Сохраняем выполненные задачи
print(task.spisok1)  # Выводим список выполненных задач