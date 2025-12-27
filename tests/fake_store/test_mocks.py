import pytest
from tests.fake_store.mocks.requests_mock import FakeStoreAPIMocks


def test_mocks_work():
    """Проверяем, что моки возвращают корректные данные"""
    mock_response = FakeStoreAPIMocks.mock_successful_product_create()

    assert mock_response.status_code == 201
    data = mock_response.json()
    assert data["id"] == 21
    assert "title" in data
    assert "price" in data
    assert data["price"] == 13.5
    print("\nAll asserts passed!")