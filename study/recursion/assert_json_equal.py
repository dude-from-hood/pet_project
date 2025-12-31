import json
from copy import deepcopy
from pytest_check import check


def assert_json_equal(actual_response, expected_result, ignore_params=None, ignore_order=True, msg_prefix=""):
    """
    Сравнивает JSON-структуры через pytest-check для детальных отчетов

    Args:
        actual_response: dict/list - реальный ответ от API
        expected_result: dict/list - ожидаемая структура
        ignore_params: list[str] - поля для игнорирования (на всех уровнях)
        ignore_order: bool - игнорировать порядок в списках (True по умолчанию)
        msg_prefix: str - префикс для сообщений об ошибках (например, "API /users")

    Returns:
        bool: True если структуры совпадают с учётом настроек
    """
    ignore_params = set(ignore_params or [])
    errors = []

    # Глубокое копирование для безопасности
    actual_clean = _remove_ignore_params(deepcopy(actual_response), ignore_params)
    expected_clean = _remove_ignore_params(deepcopy(expected_result), ignore_params)

    _compare_recursive(
        actual_clean,
        expected_clean,
        path=["root"],
        errors=errors,
        ignore_order=ignore_order
    )

    # Регистрируем все ошибки через pytest-check
    for error in errors:
        full_msg = f"{msg_prefix}: {error}" if msg_prefix else error
        check.fail(full_msg)  # Не прерывает тест, собирает все ошибки

    return not errors


# Остальные вспомогательные функции (_remove_ignore_params, _compare_recursive и т.д.)
# остаются БЕЗ ИЗМЕНЕНИЙ (берем их из вашего кода выше)


def compare_json(actual_response, expected_result, ignore_params=None, ignore_order=True):
    """
    Рекурсивно сравнивает JSON-структуры с поддержкой игнорирования полей и порядка

    Args:
        actual_response: dict/list - реальный ответ от API
        expected_result: dict/list - ожидаемая структура
        ignore_params: list[str] - поля для игнорирования (на всех уровнях)
        ignore_order: bool - игнорировать порядок в списках (True по умолчанию)

    Returns:
        bool: True если структуры совпадают с учётом настроек
    """
    ignore_params = set(ignore_params or [])
    errors = []

    # Глубокое копирование для безопасности
    actual_clean = _remove_ignore_params(deepcopy(actual_response), ignore_params)
    expected_clean = _remove_ignore_params(deepcopy(expected_result), ignore_params)

    _compare_recursive(
        actual_clean,
        expected_clean,
        path=["root"],
        errors=errors,
        ignore_order=ignore_order
    )

    if errors:
        print("❌ Найдены расхождения:")
        for error in errors:
            print(f"   • {error}")
        return False

    print("✅ Все проверки пройдены успешно")
    return True


def _remove_ignore_params(obj, ignore_params):
    """Рекурсивно удаляет игнорируемые поля из структуры"""
    if isinstance(obj, dict):
        return {
            k: _remove_ignore_params(v, ignore_params)
            for k, v in obj.items()
            if k not in ignore_params
        }
    elif isinstance(obj, list):
        return [_remove_ignore_params(item, ignore_params) for item in obj]
    return obj


def _compare_recursive(actual, expected, path, errors, ignore_order):
    """Основная логика сравнения с накоплением ошибок"""
    # 1. Проверка типов (строгая)
    if type(actual) != type(expected):
        errors.append(
            f"{_format_path(path)}: типы не совпадают "
            f"(ожидался {type(expected).__name__}, получен {type(actual).__name__})"
        )
        return

    # 2. Сравнение словарей
    if isinstance(expected, dict):
        _compare_dicts(actual, expected, path, errors, ignore_order)

    # 3. Сравнение списков
    elif isinstance(expected, list):
        _compare_lists(actual, expected, path, errors, ignore_order)

    # 4. Сравнение примитивов
    else:
        # Особый случай: str vs int/float
        if isinstance(expected, (int, float)) and isinstance(actual, str):
            try:
                actual_num = float(actual) if '.' in actual else int(actual)
                if actual_num != expected:
                    _add_value_mismatch_error(path, expected, actual, errors)
            except (ValueError, TypeError):
                _add_value_mismatch_error(path, expected, actual, errors)
        elif actual != expected:
            _add_value_mismatch_error(path, expected, actual, errors)


def _compare_dicts(actual, expected, path, errors, ignore_order):
    """Сравнение словарей после удаления игнорируемых полей"""
    exp_keys = set(expected.keys())
    act_keys = set(actual.keys())

    # Отсутствующие ключи
    for key in (exp_keys - act_keys):
        errors.append(f"{_format_path(path + [key])}: отсутствует в ответе")

    # Лишние ключи
    for key in (act_keys - exp_keys):
        errors.append(f"{_format_path(path + [key])}: лишний ключ в ответе")

    # Рекурсия для общих ключей
    for key in (exp_keys & act_keys):
        _compare_recursive(
            actual[key],
            expected[key],
            path + [key],
            errors,
            ignore_order
        )


def _compare_lists(actual, expected, path, errors, ignore_order):
    """Сравнение списков с поддержкой игнорирования порядка"""
    if len(actual) != len(expected):
        errors.append(
            f"{_format_path(path)}: длина списков различается "
            f"(ожидалось {len(expected)}, получено {len(actual)})"
        )
        return

    if ignore_order:
        # Глубокое сравнение с перебором (не используем сортировку!)
        _compare_unordered_lists(actual, expected, path, errors, ignore_order)
    else:
        # Поэлементное сравнение с учётом порядка
        for i, (act_item, exp_item) in enumerate(zip(actual, expected)):
            _compare_recursive(
                act_item,
                exp_item,
                path + [i],
                errors,
                ignore_order
            )


def _compare_unordered_lists(actual, expected, path, errors, ignore_order):
    """Сравнение списков в любом порядке через парное сопоставление"""
    remaining_expected = list(enumerate(expected))
    matched_indices = set()

    for act_idx, act_item in enumerate(actual):
        found_match = False

        for exp_idx, exp_item in remaining_expected:
            if exp_idx in matched_indices:
                continue

            # Временное сравнение без накопления ошибок
            temp_errors = []
            _compare_recursive(
                act_item,
                exp_item,
                path + [act_idx],
                temp_errors,
                ignore_order
            )

            if not temp_errors:
                matched_indices.add(exp_idx)
                found_match = True
                break

        if not found_match:
            errors.append(f"{_format_path(path)}: не найдено совпадение для элемента [{act_idx}]")

    # Проверка оставшихся несопоставленных элементов
    for exp_idx, exp_item in remaining_expected:
        if exp_idx not in matched_indices:
            errors.append(f"{_format_path(path)}: лишний элемент в ожидаемом списке [{exp_idx}]")


def _add_value_mismatch_error(path, expected, actual, errors):
    """Форматирует ошибку несовпадения значений"""
    exp_val = json.dumps(expected, ensure_ascii=False)
    act_val = json.dumps(actual, ensure_ascii=False)
    errors.append(f"{_format_path(path)}: ожидалось {exp_val}, получено {act_val}")


def _format_path(path_parts):
    """Форматирует путь для вывода ошибок"""
    formatted = path_parts[0]  # "root"
    for part in path_parts[1:]:
        if isinstance(part, int):
            formatted += f"[{part}]"
        else:
            formatted += f".{part}"
    return formatted


# ================ ПРИМЕР ИСПОЛЬЗОВАНИЯ В TEST ================
if __name__ == "__main__":
    # Пример данных
    api_response = {
        "status": "success",
        "request_id": "req-9f3b2a1c",
        "timestamp": "2025-12-31T23:59:59Z",
        "data": {
            "user": {
                "id": 777123,
                "username": "alex_dev",
                "email": "alex@example.com",
                "profile": {
                    "full_name": "Alexander Petrov",
                    "country": "Kazakhstan",
                    "preferences": {
                        "theme": "dark",
                        "lang": "en",
                        "notifications": True
                    }
                }
            },
            "orders": [
                {
                    "order_id": "ORD-1002",
                    "items": [
                        {"sku": "LAPTOP-2025", "price": 1499.99, "qty": 1},
                        {"sku": "MOUSE-G7", "price": 79.50, "qty": 2}
                    ],
                    "total": 1658.99,
                    "created_at": "2025-12-30T10:15:00Z"
                },
                {
                    "order_id": "ORD-1001",
                    "items": [
                        {"sku": "KEYBOARD-MK", "price": 120.00, "qty": 1}
                    ],
                    "total": 120.00,
                    "created_at": "2025-12-29T14:22:00Z"
                }
            ],
            "metadata": {
                "last_login": "2025-12-31T20:00:00Z",
                "verified": True,
                "internal_tags": ["premium", "beta-tester", "api_v2_user"]
            }
        }
    }

    expected_data = {
        "status": "success",
        "data": {
            "user": {
                "id": 777123,
                "username": "alex_dev",
                "email": "alex@example.com",
                "profile": {
                    "full_name": "Alexander Petrov",
                    "country": "Kazakhstan",
                    "preferences": {
                        "theme": "dark",
                        "lang": "en",
                        "notifications": True
                    }
                }
            },
            "orders": [
                {
                    "order_id": "ORD-1001",
                    "items": [
                        {"sku": "KEYBOARD-MK", "price": 120.00, "qty": 1}
                    ],
                    "total": 120.00
                },
                {
                    "order_id": "ORD-1002",
                    "items": [
                        {"sku": "MOUSE-G7", "price": 79.50, "qty": 2},
                        {"sku": "LAPTOP-2025", "price": 1499.99, "qty": 1},

                    ],
                    "total": 1658.99
                }
            ],
            "metadata": {
                "verified": True,
                "internal_tags": ["beta-tester", "api_v2_user", "premium"]
            }
        }
    }

    # Собираем все ошибки вручную (имитация pytest-check)
    collected_errors = []

    # Сохраняем оригинальный check.fail
    original_check_fail = check.fail

    # Подменяем check.fail, чтобы собрать ошибки
    def capture_error(msg):
        collected_errors.append(msg)

    check.fail = capture_error

    try:
        # Вызываем функцию напрямую, как в pytest-тесте
        assert_json_equal(
            actual_response=api_response,
            expected_result=expected_data,
            ignore_params=["request_id", "timestamp", "created_at", "last_login"],
            ignore_order=True,
            msg_prefix="API /v1/users"
        )
    finally:
        # Восстанавливаем оригинальный check.fail
        check.fail = original_check_fail

    # Выводим результат
    if collected_errors:
        print("❌ Найдены расхождения:")
        for err in collected_errors:
            print(f"   • {err}")
    else:
        print("✅ Все проверки пройдены успешно")