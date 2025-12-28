import requests


class UserService:
    def get_user_from_external_api(self, user_id: int) -> dict:
        """Получает данные пользователя из внешнего API"""
        response = requests.get(url=f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def process_user_data(self, user_data: dict) -> dict:
        """Обрабатывает данные пользователя"""
        return {
            "id": user_data["id"],
            "name": user_data["name"].upper(),
            "email": user_data["email"],
            "is_active": user_data.get("active", False)
        }