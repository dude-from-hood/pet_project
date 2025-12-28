import pytest
from fastapi.testclient import TestClient
from common.bindings.app.main import app
from common.bindings.app.services.user_service import UserService


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_user_service(mocker):
    """Фикстура для создания мока сервиса"""
    mock_service = mocker.Mock(spec=UserService)
    mock_service.get_user_from_external_api.return_value = {
        "id": 1,
        "name": "john doe",
        "email": "john@example.com",
        "active": True
    }
    mock_service.process_user_data.return_value = {
        "id": 1,
        "name": "JOHN DOE",
        "email": "john@example.com",
        "is_active": True
    }
    return mock_service

