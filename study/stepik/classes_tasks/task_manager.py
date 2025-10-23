class Task:
    def __init__(self, name, description, status=False):
        # Инициализация атрибутов задачи
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        # Вывод информации о задаче
        print(f"{self.name} ({'Сделана' if self.status else 'Не сделана'})")


class TaskList:
    def __init__(self):
        # Создание пустого списка задач
        self.tasks = []

    def add_task(self, task):
        # Добавление задачи в список
        self.tasks.append(task)

    def remove_task(self, task):
        # Удаление задачи из списка
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError("Задача не найдена в списке")


class TaskManager:
    def __init__(self, task_list=None):
        # Принимает экземпляр класса TaskList или создает новый, если он не передан
        if task_list is None:
            task_list = TaskList()
        self.task_list = task_list

    def mark_done(self, task):
        # Устанавливает статус выполнения задачи в True
        if not isinstance(task, Task):
            raise ValueError("Переданный объект не является экземпляром класса Task")
        task.status = True

    def mark_undone(self, task):
        # Устанавливает статус выполнения задачи в False
        if not isinstance(task, Task):
            raise ValueError("Переданный объект не является экземпляром класса Task")
        task.status = False

    def show_tasks(self):
        # Выводит информацию о всех задачах в списке
        for task in self.task_list.tasks:
            task.display()


if __name__ == '__main__':
    # Создаем задачи
    task1 = Task("Задача 1", "Описание задачи 1")
    task2 = Task("Задача 2", "Описание задачи 2")

    # Выводим статус задач
    task1.display()  # Задача 1 (Не сделана)
    task2.display()  # Задача 2 (Не сделана)

    # Создаем список задач
    task_list = TaskList()

    # Добавляем задачи в список
    task_list.add_task(task1)
    task_list.add_task(task2)

    # Создаем менеджер задач
    manager = TaskManager(task_list)

    # Отображаем все задачи
    print("Все задачи:")
    manager.show_tasks()

    # Отмечаем первую задачу как выполненную
    manager.mark_done(task1)

    # Отображаем все задачи снова
    print("\nПосле отметки первой задачи как выполненной:")
    manager.show_tasks()

    # Отмечаем вторую задачу как невыполненную
    manager.mark_undone(task2)

    # Отображаем все задачи снова
    print("\nПосле отметки второй задачи как невыполненной:")
    manager.show_tasks()

