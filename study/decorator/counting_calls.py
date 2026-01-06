from functools import wraps
from typing import Callable


def counting_calls(func: Callable):
    @wraps(func)
    def inner(*args, **kwargs):
        # Инициализируем счетчик и список вызовов, если они не существуют
        if not hasattr(inner, 'call_count'):
            inner.call_count = 0
        if not hasattr(inner, 'calls'):
            inner.calls = []

        # Увеличиваем счетчик вызовов
        inner.call_count += 1

        # Сохраняем аргументы в формате словаря
        call_info = {
            'args': args,
            'kwargs': kwargs
        }
        inner.calls.append(call_info)

        # Вызываем оригинальную функцию
        return func(*args, **kwargs)

    return inner


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])
print(add.calls)