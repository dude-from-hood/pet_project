from common.bindings.app.services.user_service import UserService


class TestUserClient:

    def test_get_user_success(self, client, mocker, mock_user_service):
        """
        Тестируем успешный сценарий
        """

        # Заменяем реальный экземпляр сервиса на мок
        mocker.patch('common.bindings.app.main.user_service', mock_user_service)

        # Act
        response = client.get("/users/1")

        # Assert
        assert response.status_code == 200
        assert response.json()["status"] == "success"
        assert response.json()["data"] == mock_user_service.process_user_data.return_value

        # Проверяем, что методы были вызваны
        mock_user_service.get_user_from_external_api.assert_called_once_with(1)
        mock_user_service.process_user_data.assert_called_once()

    def test_get_user_external_api_fails(self, client, mocker, mock_user_service):
        """
        Тестируем сценарий, когда внешний API падает
        """

        # Arrange
        user_id = 999

        # Мокаем метод так, чтобы он бросал исключение
        mock_user_service.get_user_from_external_api.side_effect = Exception("External API is down")

        # Заменяем реальный экземпляр сервиса на мок
        mocker.patch('common.bindings.app.main.user_service', mock_user_service)

        # Act
        response = client.get(f"/users/{user_id}")

        # Assert
        assert response.status_code == 500
        assert "External API is down" in response.json()["detail"]

    #
    # # Тест с использованием spy для отслеживания вызовов
    # def test_get_user_with_spy(self, client, mocker):
    #     """
    #     Используем spy для отслеживания вызовов реального метода
    #     """
    #     # Arrange
    #     user_id = 2
    #     mock_response_data = {
    #         "id": user_id,
    #         "name": "jane doe",
    #         "email": "jane@example.com",
    #         "active": True
    #     }
    #
    #     # Создаем spy на методе process_user_data
    #     # Spy оборачивает реальный метод, но позволяет отслеживать вызовы
    #     spy_process_user = mocker.spy(UserService, 'process_user_data')
    #
    #     # Мокаем только get_user_from_external_api
    #     mocker.patch.object(
    #         UserService,
    #         'get_user_from_external_api',
    #         return_value=mock_response_data
    #     )
    #
    #     # Act
    #     response = client.get(f"/users/{user_id}")
    #
    #     # Assert
    #     assert response.status_code == 200
    #
    #     # Проверяем, что process_user_data был вызван
    #     spy_process_user.assert_called_once()
    #
    #     # Проверяем с каким аргументом был вызван метод
    #     call_args = spy_process_user.call_args
    #     assert call_args[0][1] == mock_response_data  # Второй аргумент (первый - self)
    #
    #
    # # Тест с моком на requests (более низкий уровень)
    # def test_get_user_mocking_requests_directly(self, client, mocker):
    #     """
    #     Пример мока на уровне библиотеки requests
    #     """
    #     # Arrange
    #     user_id = 3
    #
    #     # Мокаем requests.get напрямую
    #     mock_requests_get = mocker.patch('app.services.user_service.requests.get')
    #
    #     # Настраиваем mock response
    #     mock_response = mocker.Mock()
    #     mock_response.json.return_value = {
    #         "id": user_id,
    #         "name": "bob smith",
    #         "email": "bob@example.com",
    #         "active": False
    #     }
    #     mock_response.raise_for_status = mocker.Mock()  # Мокаем метод без исключений
    #
    #     mock_requests_get.return_value = mock_response
    #
    #     # Act
    #     response = client.get(f"/users/{user_id}")
    #
    #     # Assert
    #     assert response.status_code == 200
    #
    #     # Проверяем, что requests.get был вызван с правильным URL
    #     mock_requests_get.assert_called_once_with(f"https://api.example.com/users/{user_id}")
    #
    #
    # # Параметризованный тест
    # @pytest.mark.parametrize("user_id,expected_name", [
    #     (1, "JOHN DOE"),
    #     (2, "JANE DOE"),
    #     (3, "BOB SMITH"),
    # ])
    # def test_get_user_parametrized(self, client, mocker, user_id, expected_name):
    #     """
    #     Параметризованный тест для разных пользователей
    #     """
    #     # Arrange
    #     mock_response_data = {
    #         "id": user_id,
    #         "name": expected_name.lower(),
    #         "email": f"user{user_id}@example.com",
    #         "active": True
    #     }
    #
    #     mocker.patch.object(
    #         UserService,
    #         'get_user_from_external_api',
    #         return_value=mock_response_data
    #     )
    #
    #     # Act
    #     response = client.get(f"/users/{user_id}")
    #
    #     # Assert
    #     assert response.status_code == 200
    #     assert response.json()["data"]["name"] == expected_name
    #
    #
    # # Фикстура для общих моков
    # @pytest.fixture
    # def mocked_user_service(mocker):
    #     """Фикстура, которая создает мок сервиса"""
    #     mock_service = mocker.Mock(spec=UserService)
    #     mock_service.get_user_from_external_api.return_value = {
    #         "id": 1,
    #         "name": "test user",
    #         "email": "test@example.com",
    #         "active": True
    #     }
    #     mock_service.process_user_data.return_value = {
    #         "id": 1,
    #         "name": "TEST USER",
    #         "email": "test@example.com",
    #         "is_active": True
    #     }
    #     return mock_service
    #
    #
    # def test_get_user_with_fixture(client, mocker, mocked_user_service):
    #     """
    #     Тест с использованием фикстуры для мока
    #     """
    #     # Заменяем реальный экземпляр сервиса на мок
    #     mocker.patch('app.main.user_service', mocked_user_service)
    #
    #     # Act
    #     response = client.get("/users/1")
    #
    #     # Assert
    #     assert response.status_code == 200
    #     mocked_user_service.get_user_from_external_api.assert_called_once_with(1)
    #     mocked_user_service.process_user_data.assert_called_once()