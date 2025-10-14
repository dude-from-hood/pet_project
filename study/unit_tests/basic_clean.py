def is_positive_even(number: int) -> bool:
    """Проверяет, что число положительное, чётное и <= 1000."""
    return 1000 >= number > 0 and number % 2 == 0

# Простые функции-проверки (возвращают True/False)
def check_positive_even():
    return is_positive_even(4) is True

def check_positive_odd():
    return is_positive_even(3) is False

def check_max_boundary():
    return is_positive_even(1000) is True

def check_neg_boundary():
    return is_positive_even(2001) is True # тут проверка на дурака - чтобы print выдал False

def check_above_limit():
    return is_positive_even(9999) is False

# def test_positive_even(): # Достаточно префикса test_ в имени функции и сразу запуститься pytest
#     return is_positive_even(54) is True



#+------------------------
def sum_params(a, b):
    return a + b

def check_sum_func(n, m, total):

    if None in [n, m, total]:
        raise ValueError("Null передан во входные параметры")

    if not all(isinstance(x, int) for x in (n, m, total)):
        raise TypeError("Тип данных не integer")

    if not sum_params(n, m) == total:
        raise AssertionError("Значения total неверно")

    else:
        return True

# Запуск проверок
if __name__ == '__main__':
    print(check_sum_func(3, 2, 5))

    #
    # print("Проверка чётного положительного:", check_positive_even())
    # print("Проверка нечётного:", check_positive_odd())
    # print("Проверка граничного значения (1000):", check_max_boundary())
    # print("Заведомо негативная проверка (2001):", check_neg_boundary())
    # print("Проверка превышения лимита (9999):", check_above_limit())
    #
    # # print("Проверка функции is_positive_even")
    # number = is_positive_even(int(input()))
    # print(number)
