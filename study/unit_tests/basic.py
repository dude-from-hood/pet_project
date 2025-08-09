import unittest

def is_positive_even(number: int) -> bool:
    """Проверяет, является ли число положительным чётным числом."""

    return number > 0 and number % 2 == 0
class TestIsEven(unittest.TestCase):
    def test_positive_even(self):
        self.assertTrue(is_positive_even(4))  # базовый кейс

    def test_positive_odd(self):
        self.assertFalse(is_positive_even(3))  # положительное, но нечётное

    def test_negative_even(self):
        self.assertFalse(is_positive_even(-2))  # чётное, но отрицательное

    def test_zero(self):
        self.assertFalse(is_positive_even(0))  # граничный случай (не положительное тк 0 = нейтральное число)

    def test_large_number(self):
        self.assertTrue(is_positive_even(1000))  # большое число

# Запуск тестов:
# python -m unittest test_module.py