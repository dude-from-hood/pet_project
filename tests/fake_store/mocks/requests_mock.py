"""
Моки для стабильного запуска тестов в CI
"""

from unittest.mock import Mock


class FakeStoreAPIMocks:
    """Моки для API fakestoreapi.com"""

    @staticmethod
    def mock_successful_product_create():
        """Мок успешного создания продукта"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": 21,
            "title": "test product",
            "price": 13.5,
            "description": "lorem ipsum set",
            "image": "https://i.pravatar.cc",
            "category": "electronic"
        }
        return mock_response

    @staticmethod
    def mock_get_products():
        """Мок получения списка продуктов"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": 1,
                "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                "price": 109.95,
                "description": "Your perfect pack for everyday use and walks in the forest...",
                "category": "men's clothing",
                "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
            }
        ]
        return mock_response

    @staticmethod
    def mock_get_product():
        """Мок получения одного продукта"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest...",
            "category": "men's clothing",
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
        }
        return mock_response

    @staticmethod
    def mock_update_product():
        """Мок обновления продукта"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 7,
            "title": "White Gold Plated Princess",
            "price": 9.99,
            "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"
        }
        return mock_response

    @staticmethod
    def mock_delete_product():
        """Мок удаления продукта"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 7,
            "title": "White Gold Plated Princess",
            "price": 9.99,
            "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"
        }
        return mock_response