import logging
import sys


def setup_logger(name=__name__, level=logging.DEBUG):
    """
    Настраивает и возвращает логгер с форматом

    Args:
        name: имя логгера (обычно __name__)
        level: уровень логирования (по умолчанию DEBUG)

    Returns:
        Настроенный логгер
    """
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Проверяем, нет ли уже обработчиков (чтобы избежать дублирования)
    if logger.handlers:
        logger.handlers.clear()

    # Создаем обработчик для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Создаем красивый форматтер
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(console_handler)

    return logger
