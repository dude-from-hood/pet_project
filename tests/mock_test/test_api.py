import requests

from common.bindings.utils.create_logger import setup_logger

#+-------------------------------
logger = setup_logger(__name__)
#+-------------------------------

class TestCrud:

    def test_api_with_valid_auth(self, valid_auth_headers, mock_requests):
        """Тест с валидной авторизацией"""

        logger.info("Запрос готов")
        response = requests.get(
            "https://api.example.com/protected",
            headers=valid_auth_headers
        )
        logger.info("Запрос отправлен")

        assert response.status_code == 200
        assert response.json()["data"] == "test"
        # Проверяем, что заголовки были переданы
        mock_requests["get_mock"].assert_called_once()

    def test_api_with_expired_token(self, expired_auth_headers, mock_requests):
        """Тест с просроченным токеном"""
        response = requests.get(
            "https://api.example.com/protected",
            headers=expired_auth_headers
        )

        assert response.status_code == 200
        assert "expired_token_" in expired_auth_headers["Authorization"]

    def test_auth_endpoint(self, mock_requests):
        """Тест endpoint авторизации"""
        auth_data = {"username": "test", "password": "test"}
        response = requests.post(
            "https://api.example.com/auth",
            json=auth_data
        )

        assert response.status_code == 201
        assert "id" in response.json()
        assert "token" in response.json()

    def test_put_request(self, valid_auth_headers, mock_requests):
        """Тест PUT-запроса с авторизацией"""
        update_data = {"name": "new_name"}
        response = requests.put(
            "https://api.example.com/user/123",
            json=update_data,
            headers=valid_auth_headers
        )

        assert response.status_code == 200
        assert response.json()["updated"] is True

    def test_delete_request(self, valid_auth_headers, mock_requests):
        """Тест DELETE-запроса с авторизацией"""
        response = requests.delete(
            "https://api.example.com/user/123",
            headers=valid_auth_headers
        )

        assert response.status_code == 204