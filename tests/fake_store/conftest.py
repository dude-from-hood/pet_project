import allure
import pytest
from unittest.mock import patch, Mock
from tests.fake_store.mocks.requests_mock import FakeStoreAPIMocks
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

            # Используем indirect=True, чтобы параметры передавались в фикстуру
            # Это позволяет фикстуре генерировать данные при каждом запуске теста
            metafunc.parametrize(fixture, res, indirect=True)


def _generate_test_data_from_config(test_data_config):
    """
    Универсальная функция для генерации тестовых данных из конфигурации.
    Поддерживает два формата:
    1. Новый: с ключом 'test_data_generator' - функция генерации вызывается при каждом запуске
    2. Старый: с ключом 'test_data' - данные уже сгенерированы (для обратной совместимости)
    """
    test_data_config = test_data_config.copy()
    
    # Если есть функция генерации, вызываем её для создания новых данных
    if 'test_data_generator' in test_data_config:
        test_data_config['test_data'] = test_data_config['test_data_generator']()
        # Удаляем генератор, чтобы не передавать его в тест
        del test_data_config['test_data_generator']
    # Если данных нет и нет генератора, это ошибка конфигурации
    elif 'test_data' not in test_data_config:
        raise ValueError(
            "В конфигурации тестовых данных должен быть либо 'test_data', "
            "либо 'test_data_generator'"
        )
    # Если данные уже есть (старый формат), используем их как есть
    
    return test_data_config


@pytest.fixture(scope="function")
def data_test_create_product(request):
    """
    Фикстура, которая генерирует тестовые данные при каждом запуске теста.
    Это обеспечивает перегенерацию данных при ретраях через pytest-rerun-failures.
    """
    return _generate_test_data_from_config(request.param)


@pytest.fixture(autouse=True)
def mock_external_apis():
    """
    Автоматически заглушаем все внешние API запросы в тестах.
    Это делает тесты стабильными и независимыми от внешних сервисов.
    """
    with patch('requests.post') as mock_post, \
            patch('requests.get') as mock_get, \
            patch('requests.put') as mock_put, \
            patch('requests.delete') as mock_delete:
        # Настраиваем моки для разных URL

        # POST запросы
        mock_post.return_value = FakeStoreAPIMocks.mock_successful_product_create()

        # GET запросы (продукты)
        mock_get.side_effect = lambda url, **kwargs: (
            FakeStoreAPIMocks.mock_get_products()
            if 'products' in url and not url.endswith('/1')
            else FakeStoreAPIMocks.mock_get_product()
        )

        # PUT запросы
        mock_put.return_value = FakeStoreAPIMocks.mock_update_product()

        # DELETE запросы
        mock_delete.return_value = FakeStoreAPIMocks.mock_delete_product()

        yield