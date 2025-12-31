import time
from functools import wraps


def execution_time_deco(func):
    @wraps(func)  # создаем декоратор
    def wrapper():
        print("Функция начинает свою работу!")
        start = time.time()          # Замер до вызова
        result = func()              # Выполняем функцию
        finish = time.time()         # Замер после вызова
        duration = finish - start
        print(f"Время выполнения: {duration:.6f} сек")
        print("Функция закончила свою работу")
        return result                # Возвращаем результат функции, а не время
    return wrapper

@execution_time_deco
def my_func():
    """важный docstring"""
    s = [i for i in range(1000000)]  # пример полезной работы
    return "Готово!"

print(my_func()) # выводим результат функции

print(my_func.__name__)
print(my_func.__doc__)