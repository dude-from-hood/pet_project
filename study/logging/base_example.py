from common.bindings.utils.create_logger import setup_logger

# Использование
logger = setup_logger(__name__)

def divide_numbers(a, b):
    logger.info(f"Вызвана функция divide_numbers с аргументами: a={a}, b={b}")
    try:
        result = a / b
        logger.debug(f"Результат деления: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Попытка деления на ноль!", exc_info=True) # exc_info=True добавит traceback
        return None

# Использование
divide_numbers(10, 2)
divide_numbers(10, 0)
