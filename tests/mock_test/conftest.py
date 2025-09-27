import pytest
import requests
from study.mock_auth_token.auth_utils import generate_fake_token, generate_expired_token


# Фикстуры для заголовков авторизации
@pytest.fixture
def valid_auth_headers():
    """Фикстура с валидными заголовками авторизации"""
    token = generate_fake_token("test_user")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def expired_auth_headers():
    """Фикстура с просроченным токеном"""
    token = generate_expired_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def mock_requests(mocker):
    """Фикстура для мокинга requests"""

    def mock_response(status_code=200, json_data=None, text=None):
        response = mocker.Mock()
        response.status_code = status_code
        response.json.return_value = json_data or {}
        response.text = text or ""
        return response

    # Мок для успешного GET-запроса
    mocker.patch.object(
        requests,
        'get',
        return_value=mock_response(200, {"data": "test"})
    )

    # Мок для POST-запроса
    mocker.patch.object(
        requests,
        'post',
        return_value=mock_response(201, {"id": 123, "token": "fake_token_123"})
    )

    # Мок для PUT-запроса
    mocker.patch.object(
        requests,
        'put',
        return_value=mock_response(200, {"updated": True})
    )

    # Мок для DELETE-запроса
    mocker.patch.object(
        requests,
        'delete',
        return_value=mock_response(204)
    )

    # Можно вернуть моки для использования в тестах
    return {
        "get_mock": requests.get,
        "post_mock": requests.post,
        "put_mock": requests.put,
        "delete_mock": requests.delete
    }

@pytest.fixture(scope='session', autouse=True)
def clean_up_test_data():
    yield
    print()
    print("Тестовые данные удалены")
