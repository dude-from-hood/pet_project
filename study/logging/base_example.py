from common.bindings.utils.create_logger import log

def divide_numbers(a, b):
    log.info(f"Вызвана функция divide_numbers с аргументами: a={a}, b={b}")
    try:
        result = a / b
        log.info(f"Результат деления: {result}")
        return result
    except ZeroDivisionError:
        log.error("Попытка деления на ноль!", exc_info=True) # exc_info=True добавит traceback
        return None

# Использование
divide_numbers(10, 2)
divide_numbers(10, 0)
