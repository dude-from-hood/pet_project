import requests
import pytest
import responses
from pytest_check import check


# 1. Определяем сценарии
SCENARIOS = [
    {"user_id": 123, "expected_name": "Bob", "status": 200},
    {"user_id": 456, "expected_name": "Alice", "status": 200},
    {"user_id": 999, "expected_name": None, "status": 404},
]


# 2. Параметризованная фикстура — создаёт мок только для одного сценария
@pytest.fixture(params=SCENARIOS, ids=lambda s: f"user_{s['user_id']}")
def mock_user_api(request):
    scenario = request.param
    user_id = scenario["user_id"]
    status = scenario["status"]
    url = f"https://api.example.com/users/{user_id}"

    with responses.RequestsMock() as rsps:
        if status == 200:
            rsps.add("GET", url, json={"name": scenario["expected_name"]}, status=200)
        else:
            rsps.add("GET", url, json={"error": "User not found"}, status=404)
        # Передаём сценарий в тест, чтобы знать, чего ожидать
        yield rsps, scenario


# 3. Тест — получает и мок, и данные сценария
def test_fetch_user(mock_user_api):
    rsps, scenario = mock_user_api
    user_id = scenario["user_id"]
    expected_name = scenario["expected_name"]
    expected_status = scenario["status"]

    resp = requests.get(f"https://api.example.com/users/{user_id}")

    # Проверки
    check.equal(resp.status_code, expected_status)

    if expected_status == 200:
        check.equal(resp.json()["name"], expected_name)
    else:
        check.is_true("error" in resp.json())

    # Убедимся, что запрос был перехвачен
    assert len(rsps.calls) == 1
