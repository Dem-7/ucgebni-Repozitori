class Task:
    tasks = []

    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    @classmethod
    def add_task(cls, description, deadline):

        new_task = cls(description, deadline)
        cls.tasks.append(new_task)
        return new_task

    def mark_as_done(self):

        self.status = True

    @classmethod
    def show_current_tasks(cls):

        current_tasks = [task for task in cls.tasks if not task.status]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            print("Текущие задачи:")
            for task in current_tasks:
                print(f"- {task.description} (Срок: {task.deadline})")



Task.add_task("Купить продукты", "2025-03-05")
Task.add_task("Подготовить отчет", "2025-03-22")


Task.show_current_tasks()


task_to_done = Task.tasks[0]
task_to_done.mark_as_done()


Task.show_current_tasks()
