import importlib.util
import os

import allure
import pytest

import config

"""
Разделение на load_tests и pytest_generate_tests нужно для следующего:

1. pytest_generate_tests - это хук pytest, который вызывается при инициализации тестов. 
    Он отвечает за параметризацию тестов (например, передачу данных в тест через фикстуры).
    
2. load_tests - это вспомогательная функция, 
    которая отвечает за загрузку тестовых данных из внешнего файла (например, .py-файла с тестовыми данными).
"""


def pytest_generate_tests(metafunc):
    """
    Хук, который при инициализации фикстур, смотрит есть ли у теста фикстуры, начинающиеся с data_,
    если находит - импортирует фикстуру, как пакет.

    Если в тесте есть фикстура data_create_product
     И res = [{'name': 'laptop', 'price': 1000}, {'name': 'phone', 'price': 500}]

    Тогда создаются два теста:
     test_create_product(data_create_product={'name': 'laptop', 'price': 1000})
     test_create_product(data_create_product={'name': 'phone', 'price': 500})
    """

    # перебираем фикстуры
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):

            # передаем название параметра в функцию, которая парсит файл
            tests = load_tests(fixture)

            # пробрасываем allure description и обрабатываем xfail
            res = []
            for test_data in tests:  # перебираем тестовые данные
                allure.dynamic.description(test_data['description'])

                if test_data.get('xfail') is not None:
                    test_data = pytest.param(test_data, marks=pytest.mark.xfail(
                        strict=True,
                        reason=test_data['xfail'].get('jira')
                    ))

                res.append(test_data)

            # пробрасываем данные в тест
            metafunc.parametrize(fixture, res)


def load_tests(name_of_data_file: str, path: str):
    """
    Функция отвечает за загрузку тестовых данных из внешних Python-файлов.

    Что делает load_tests:
    1. Принимает имя файла данных (name_of_data_file) и путь к нему (path)
    2. Собирает полный путь к файлу данных
    3. Импортирует файл как модуль Python
    4. Возвращает данные из test_data в виде генератора

    Итог: мы получаем доступ к test_data из файла, но делаем это безопасным способом
    """

    # абсолютный путь к тестовым данным
    file_path = os.path.join(config.ROOT, path, f"{name_of_data_file}.py")  # в конфиге хранится os путь до файла

    # создание спецификации модуля
    """
    Зачем это нужно:
        Безопасность - позволяет загрузить модуль без выполнения его кода сразу
        Контроль - дает возможность проверить, что модуль существует и корректен
    """
    spec = importlib.util.spec_from_file_location(name_of_data_file, file_path)

    if spec is None:
        raise ImportError(f"Cannot find module {name_of_data_file} at {file_path}")

    # создание модуля из спецификации
    """
    Здесь уже происходит реальная загрузка модуля с выполнением его кода, 
     и в tests_module оказывается объект, содержащий test_data.
    """
    tests_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests_module)

    # возвращаем данные из test_data как генератор, имя test_data - это соглашение о названии переменной, содержащей набор тестовых данных
    for param in tests_module.test_data:
        yield param
