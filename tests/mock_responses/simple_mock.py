import responses
import requests

with responses.RequestsMock() as mock_resp:
    """
    Контекстный менеджер для изолированного мокирования HTTP-запросов.

    Используется для перехвата вызовов библиотеки `requests` внутри блока,
    предотвращая реальные сетевые запросы. Позволяет задать фиксированные
    ответы (статус, заголовки, тело) для конкретных URL и методов,
    что обеспечивает быстрое, детерминированное и независимое от сети
    тестирование клиентского кода.

    Все зарегистрированные моки автоматически удаляются после выхода из блока.
    """
    mock_resp.get("https://api.example.com/user/42", json={"name": "Bob"}, status=200)

    resp = requests.get("https://api.example.com/user/42")
    assert resp.json()["name"] == "Bob"

    print(resp.json())
