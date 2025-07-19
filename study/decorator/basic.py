"""
Декоратор — это функция, которая позволяет обогатить любую другую функцию дополнительным поведением без необходимости изменения ее кода.
Декоратор очень часто называют оберткой для функции, потому что он оборачивает ее и позволяет добавить новый функционал как перед вызовом функции,
  так и после завершения ее работы.

Чтобы создать декоратор, необходимо определить внешнюю функцию, которая будет принимать функцию в качестве аргумента.
Затем внутри внешней функции необходимо создать внутреннюю функцию, в которой будет происходить вызов декорированной функции.

После уже можно повестить тег на функцию с именем обертки (декоратора) при вызове, порядок исполнения см.ниже:



Порядок выполнения декораторов снизу вверх: сперва выполняется декоратор, стоящий над определением функции, но
исполнение может быть сверху вниз! - см задачу first_validator, аналогия с матрешкой.

Выполнение по принципу LIFO (Last In, First Out) — последний добавленный декоратор выполняется первым.
@decorator3
@decorator2
@decorator1
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


@repeater  # вот такой тег
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
            return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}  # после ключа пишем условие

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


def first_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print(f"Важная проверка не пройдена")
            return None
        print(f"Заканчиваем важную проверку")

    return my_wrapper


def second_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем самую важную проверку")
        if kwargs.get('name') == 'Boris':
            func(*args)  # это уже задекорированная first_validator версия sum_values
        else:
            print(f"Самая важная проверка не пройдена")
            return None
        print(f"Заканчиваем самую важную проверку")

    return my_wrapper


# используйте декораторы
@second_validator
@first_validator
def sum_values(*args):
    print(f'Получили результат равный {sum(args)}')


"""
Начинаем самую важную проверку
Начинаем важную проверку
Получили результат равный 77
Заканчиваем важную проверку
Заканчиваем самую важную проверку
"""

# вызовите функцию sum_values()
#sum_values(1, 6, 70, name='Boris')

def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                print("Все аргументы должны быть строками")
                return None
        return func(*args, **kwargs)
    return wrapper


def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        for value in kwargs.values():
            if not isinstance(value, int) or value <= 0:
                print("Все именованные аргументы должны быть положительными числами")
                return None
        return func(*args, **kwargs)
    return wrapper


@validate_all_args_str
@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result

# print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
# print(concatenate('fff', 'sss', "ss"))
# print(concatenate(a=10, b=20, c=50))


"""
Сначала filter_even фильтрует позиционные аргументы
Затем delete_short фильтрует именованные аргументы
Наконец, вызывается основная функция concatenate
"""
def filter_even(func):
    def wrapper(*args, **kwargs):  # Фильтруются только args! (позиционные аргументы)
        filtered_args = []
        for arg in args:
            if (isinstance(arg, (int, float)) and arg % 2 == 0) or (arg is False) or (
                    hasattr(arg, '__len__') and len(arg) % 2 == 0):
                filtered_args.append(arg)
        return func(*filtered_args, **kwargs)

    return wrapper

def delete_short(func):
    def wrapper(*args,**kwargs): # Фильтруются только kwargs! (именованные аргументы)
        filtered_kwargs = dict()
        for key, value in kwargs.items():
            if len(key) > 4:
                filtered_kwargs[key] = value
        return func(*args, **filtered_kwargs)

    return wrapper

@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))
# Теперь выведет: "хочу10"






