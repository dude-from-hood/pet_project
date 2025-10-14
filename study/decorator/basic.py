"""
Декоратор — это функция, которая позволяет обогатить любую другую функцию дополнительным поведением
    без необходимости изменения ее кода.
Декоратор очень часто называют оберткой для функции, потому что он оборачивает ее
    и позволяет добавить новый функционал как перед вызовом функции, так и после завершения ее работы.

Чтобы создать декоратор, необходимо определить внешнюю функцию, которая будет принимать функцию в качестве аргумента.
Затем внутри внешней функции необходимо создать внутреннюю функцию, в которой будет происходить вызов декорированной функции.

После уже можно повестить тег на функцию с именем обертки (декоратора) при вызове, порядок исполнения см.ниже:
"""
from typing import Callable
import time

from common.bindings.utils.create_logger import setup_logger

#+=================================
# Константы
logger = setup_logger()
#+=================================

#Задача №1: "Волшебный приветственник"
def my_deco(func: Callable):  # создаем декоратор
    def wrapper():
        print("Функция начинает свою работу!")
        res = func()
        return res

    return wrapper


@my_deco
def my_func():
    print("Привет, я функция!")


my_func()
print('=' * 50)


#+-------------------------------------
#Задача №2: функция c параметрами
def my_deco_func_params(func: Callable):  # создаем декоратор
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@my_deco_func_params
def greet(name, surname):
    print(f"Привет, {name} {surname}!")


greet("Anna", "Smith")
print('=' * 50)


#+-------------------------------------
#Задача №3: "Декоратор-секундомер"
#создаем декоратор-функцию
def timer(func: Callable):
    def wrapper(*args, **kwargs):
        print("Засекаем время...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Функция выполнялась {end - start} секунд")
        return res

    return wrapper


#вешаем декоратор на нужную функцию
@timer
def slow_function(seconds):
    time.sleep(seconds)
    print(f"Я поспал {seconds} секунд")


#slow_function(2)
print('=' * 50)


#+-------------------------------------
#Задача №4: "Умный декоратор с аргументами"
def deco_repeat(n: int):
    # здесь нужно вернуть декоратор
    def wrapper(func: Callable):
        def inner_wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@deco_repeat(3)
def say_hello():
    print("Привет!")


say_hello()
print('=' * 50)


#+-------------------------------------

#Задача №5: "Декоратор-ограничитель"
def limit_calls(limit: int):
    def wrapper(func: Callable):
        def inner_wrapper(*args, **kwargs):
            # переменная принадлежит не локальной области видимости этой функции, а ближайшей охватывающей (внешней) функции
            # имя такое же как во внешней функции
            nonlocal limit
            if limit == 0:
                print("Превышен лимит вызовов!")
                return

            res = func(*args, **kwargs)
            limit -= 1
            return res

        return inner_wrapper

    return wrapper


@limit_calls(3)
def say_hello():
    print("Привет!")


# say_hello()  # Работает
# say_hello()  # Работает
# say_hello()  # Превышен лимит
# say_hello()  # Превышен лимит
print('=' * 50)


#+-------------------------------------

#Задача №6: "Умный декоратор с логированием и проверкой"
# Настраиваем базовую конфигурацию логирования

def deco_logged(level: str):
    # Проверяем валидность уровня
    if level not in ('info', 'debug'):
        raise ValueError("Уровень должен быть 'info' или 'debug'")

    def wrapper(func: Callable):
        def inner_wrapper(*args, **kwargs):
            # Логируем ДО вызова функции
            if level == "info":
                logger.info(f"Вызов функции {func.__name__}")
            elif level == "debug":
                # Формируем строку с аргументами
                args_str = ", ".join([repr(arg) for arg in args])
                kwargs_str = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
                all_args = ", ".join(filter(None, [args_str, kwargs_str]))
                logger.debug(f"Вызов функции {func.__name__} с аргументами: {all_args}")

            # Вызываем функцию и возвращаем результат
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@deco_logged('info')
def add(a, b):
    return a + b


@deco_logged('debug')
def greet(name, age=None):
    if age:
        return f"Привет, {name}! Тебе {age} лет."
    return f"Привет, {name}!"


result1 = add(5, 3)
result2 = greet("Анна")
result3 = greet("Петр", age=25)

print(result1)
print(result2)
print(result3)
