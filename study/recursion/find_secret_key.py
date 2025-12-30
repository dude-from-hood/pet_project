data = {
    "level1": {
        "level2": {
            "level3": {
                "secret": "gold"  # ищем ключ
            }
        }
    }
}


def find_value_by_key(obj, target_key):
    """
    Функция рекурсивно ищет целевой ключ во вложенном словаре или списке и возвращает его значение.

    args:
    obj: Объект для поиска. Может быть словарем или списком.
    target_key: Ключ, который нужно найти.

    return:
    Значение, связанное с целевым ключом, если оно найдено; иначе возвращает None.
    """
    if isinstance(obj, dict):

        if target_key in obj:
            return obj[target_key]
        for key, value in obj.items():
            result = find_value_by_key(value, target_key) #рекурсия!
            if result is not None:
                return result

    elif isinstance(obj, list):
        for item in obj:
            result = find_value_by_key(item, target_key) #рекурсия!
            if result is not None:
                return result
    return None


print(find_value_by_key(data, "secret"))
