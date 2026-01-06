from functools import wraps
from typing import Callable


def convert_to(type_):
    """
    Декоратор convert_to, который позволяет
    автоматически преобразовать возвращаемое значение в указанный тип данных
    """
    def decorator(func: Callable):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_(result)

        return wrapper

    return decorator

@convert_to(str)
def add_values(a, b):
    return a + b


result = add_values(10, 20)
print(f"Результат: {result}, тип результата {type(result)}")

print(convert_to.__doc__)