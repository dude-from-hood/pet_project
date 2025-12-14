if __name__ == '__main__':
    import pytest

    class User:
        id: str
        username: str
        password: str

        def __init__(self, id, username, password):
            self.id = id
            self.username = username
            self.password = password

    class UserNotFound(Exception):
        ...


    class UserServiceClient(...):
        def get_user(self, user_id: str) -> User:
            """If user with given "user_id" not found will raise UserNotFound"""

        def get_users(self) -> list[User]: ...

        def create_user(self, user: User) -> User: ...

        def update_user(self, user_id: str, user: User) -> User: ...

        """If user with given "user_id" not found will raise UserNotFound"""


    def delete_user(self, user_id: str) -> None:
        """If user with given "user_id" not found will raise UserNotFound"""

class TestUserService:

    """
    Необходимо покрыть сервис 'UserService' автотестами используя библиотеку pytest
    Для взаимодействия с сервисом нужно использовать клиент `UserServiceClient`
    """

    @pytest.mark.parametrize("id, username, password, expected_result", [
        (1, 'ASd', '1234', True),
        ('sd', '123', False),
        ('1', 'ASd', '1234', False),
        (None, '123', False),
    ]
    )
    def test_user(self, id, username, password, expected_result):
        obj = User(id, username, password)
        user_serivce_obj = UserServiceClient()

        result = user_serivce_obj.create_user(obj)

        assert result == expected_result

    def test_create(self):
        ...

    def test_update(self, ):
        ...

    def test_3(self):
        ...


# GET/ UPDATE/ CREATE / DELETE
# valid values
# required fields
# invalid_type
# null

# GET_USERS
# valid