import allure
import pytest

from common.fixtures_and_hooks.fixtures import load_tests


def pytest_generate_tests(metafunc):
    """
    Хук, который при инициализации фикстур, смотрит есть ли у теста фикстуры, начинающиеся с data_,
    если находит - импортирует фикстуру, как пакет
    """

    path = 'tests/fake_store/test_data'

    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):

            # передаем название параметра в функцию, которая парсит файл
            tests = load_tests(name_of_data_file=fixture, path=path)

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

