import importlib.util
import os

import allure
import pytest

import config


def pytest_generate_tests(metafunc):
    """
    Хук, который при инициализации фикстур, смотрит есть ли у теста фикстуры, начинающиеся с data_,
    если находит - импортирует фикстуру, как пакет
    """

    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):

            # передаем название параметра в функцию, которая парсит файл
            tests = load_tests(fixture)

            # пробрасываем allure description и обрабатываем xfail
            res = []
            for test_data in tests:
                allure.dynamic.description(test_data['description'])

                if test_data.get('xfail') is not None:
                    test_data = pytest.param(test_data, marks=pytest.mark.xfail(
                        strict=True,
                        reason=test_data['xfail'].get('jira')
                    ))

                res.append(test_data)
            metafunc.parametrize(fixture, res)

def load_tests(name_of_data_file: str, path:str):
    """
    Передаем название файла (должен начинаться с data_), который будет импортирован как пакет
    """

    # абсолютный путь к тестовым данным
    file_path = os.path.join(config.ROOT, path, f"{name_of_data_file}.py") # в конфиге хранится os путь до файла

    # создание спецификации модуля
    spec = importlib.util.spec_from_file_location(name_of_data_file, file_path) # смотри на импорты в importlib.util.spec_from_file_location

    if spec is None:
        raise ImportError(f"Cannot find module {name_of_data_file} at {file_path}")

    # создание модуля из спецификации
    tests_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests_module)

    # возвращаем данные для тестов
    for param in tests_module.test_data:
        yield param



        





















