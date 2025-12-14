import pytest

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@pytest.fixture
def person(request):
    # request.param будет содержать кортеж (name, age)
    name, age = request.param
    return Person(name, age)

@pytest.mark.parametrize(
    "person, expected_category",
    [
        (("Alice", 30), "adult"),
        (("Bob", 10), "minor"),
        (("Charlie", 17), "minor"),
        (("Diana", 25), "adult")
    ],
    indirect=["person"]  # ← ТОЛЬКО 'person' идёт через фикстуру!
)

def test_person_category(person, expected_category):
    # person — объект Person (результат фикстуры)
    # expected_category — строка, передана напрямую
    if person.age >= 18:
        assert expected_category == "adult"
    else:
        assert expected_category == "minor"


@pytest.fixture
def sum_func(request):
    a, b = request.param
    return a + b

@pytest.mark.parametrize("sum_func, expected", [
    ((2, 3), 5),
    ((1, 1), 2),
    ((0, 0), 0),
    ((-1, 1), 0),
], indirect=['sum_func']
)

def test_sum(sum_func, expected):
    assert sum_func == expected


def minus_func(a, b):
    return a - b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, -1),
    (1, 1, 0),
    (0, 0, 0),
    (2, 1, 1),
    ],
)

def test_minus(a, b, expected):
    assert minus_func(a, b) == expected



try:
    # Потенциально опасный код
    file = open("file.txt", "r")
    content = file.read()

except FileNotFoundError:
    # Обработка конкретного исключения
    print("Файл не найден!")

except Exception as e:
    # Обработка всех остальных исключений
    print(f"Произошла ошибка: {e}")

else:
    # Выполняется, если исключений не было
    print("Файл успешно прочитан")

finally:
    # Выполняется всегда (с ошибкой или без)
    print("Завершение операции")