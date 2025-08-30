import pytest

# Простая фикстура, возвращающая тестовые данные
@pytest.fixture
def sample_numbers():
    """Возвращает пару чисел для тестов."""
    return (3, 5)

# Можно добавить ещё одну фикстуру — например, строку или словарь
@pytest.fixture
def sample_user():
    """Возвращает данные пользователя."""
    return {"name": "Alice", "age": 30}



"""
Если фикстура делает что-то автоматически (например, логирует начало/конец теста), 
её можно пометить как autouse=True — тогда она будет вызываться автоматически для всех тестов в скоупе, без явной передачи в параметры.
"""
@pytest.fixture(autouse=True, scope="function")
def print_before_and_after():
    print("\nStarting test...")
    yield
    print("\nGood-bye, this is the end")

"""
Фикстура с 
`scope="function"` создаётся для каждого теста (по-умолчанию это значение выбрано для scope), 
`scope="class"` — один раз на класс, 
`scope="module"` — один раз на файл, 
`scope="package"` — один раз на пакет, 
`scope="session"` — один раз на всю сессию запуска тестов.
"""