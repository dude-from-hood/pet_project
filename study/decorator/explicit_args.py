from functools import wraps

def explicit_args(func):

    @wraps(func)
    def inner(*args, **kwargs):
        """
        some docstring
        """
        if args:
            print('Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений')
            return None
        else:
            return func(*kwargs.values())
    return inner

@explicit_args
def add(a: int, b: int) -> int:
    """
    Возвращает сумму двух чисел
    """
    return a + b


print(add(10, 20))
print(dir(add))


# from typing import Callable

# def explicit_args(func: Callable) -> Callable:
#     """
#     Способ без functools - классический
#     """
#
#     def wrapper(*args, **kwargs):
#
#         if args:
#             print("Функция не принимает позиционные аргументы")
#             return None
#         return func(**kwargs)
#
#     wrapper.__doc__ = func.__doc__
#     wrapper.__name__ = func.__name__
#
#     return wrapper
