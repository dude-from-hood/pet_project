"""
Декоратор — это функция, которая позволяет обогатить любую другую функцию дополнительным поведением без необходимости изменения ее кода.
Декоратор очень часто называют оберткой для функции, потому что он оборачивает ее и позволяет добавить новый функционал как перед вызовом функции,
  так и после завершения ее работы.

Чтобы создать декоратор, необходимо определить внешнюю функцию, которая будет принимать функцию в качестве аргумента.
Затем внутри внешней функции необходимо создать внутреннюю функцию, в которой будет происходить вызов декорированной функции.

После уже можно повестить тег на функцию с именем обертки (декоратора) при вызове, порядок исполнения см.ниже:

@decorator3
@decorator2
@decorator1 - самая близкая к функции, и можно по неск.раз вещать один и тот же декоратор (два раза decorator1)
def my_function():
    pass
"""

# базовый синтаксис декоратора в python
def my_decorator(func):
    def wrapper_func():
        # Делаем что-то до вызова функции
        func()
        # Делаем что-то после вызова функции

    return wrapper_func


#декоратор repeater, который трижды вызывает декорированную функцию
def repeater(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)

    return wrapper

@repeater # вот такой тег
def multiply(num1, num2):
    return num1 * num2


# Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции
def double_it(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # сохраняем результат функции
        return result * 2  # возвращаем удвоенный результат

    return wrapper


def uppercase_elements(func):
    """
    Ваша задача написать логику работы декоратора uppercase_elements, который умеет работать с функциями, возвращающими коллекции элементов.
    Задача декоратора uppercase_elements преобразовать каждый строковый элемент коллекции к заглавному регистру.
    В случае, если оригинальная функция возвращает словарь, то элементом считаем только строковые ключи словаря.
    Элементы, не являющиеся строкой, не должны изменяться декоратором uppercase_elements

    вход:
    @uppercase_elements
    def my_func():
        return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']

    выход:
    ['MONARCH', 'TOUCH', 'OFFICIAL', 'DANGEROUS', 'BREATHE']
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        if isinstance(res, dict):
            return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()} # после ключа пишем условие

        elif isinstance(res, list):
            return [i.upper() if isinstance(i, str) else i for i in res]

        elif isinstance(res, set):
            return {i.upper() if isinstance(i, str) else i for i in res}

        elif isinstance(res, tuple):
            return tuple(
                item.upper() if isinstance(item, str) else item
                for item in res
            )
        else:
            raise ValueError("Ошибка, функция не возвращает коллекцию элементов")

    return wrapper

if __name__ == '__main__':
    def double_it(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * 2

        return wrapper


    def increment(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + 1

        return wrapper


    @double_it
    @increment
    @increment
    def add(num1, num2):
        return num1 + num2


    print(add(5, 7))

