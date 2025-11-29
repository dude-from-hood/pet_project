import os

from common.utils.random_utils import add, helper
import pytest
def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 8
    assert add(b, a) == 8

def test_user_data(sample_user):
    assert sample_user["name"] == "Alice"
    assert sample_user["age"] == 30

def test_something():
    assert 2 + 2 == 4


@pytest.mark.parametrize(
    "input_msg, max_len, expected",
    [
        ("Hi", 10, "Hi"),
        ("", 10, ""),
        ("1234567890", 10, "1234567890"),
        ("12345678901", 10, "1234567..."),
        ("A", 1, "A"),  # edge: max_len=1 → не обрезается, т.к. len=1 <= max_len
        ("AB", 1, "..."),  # len=2 > 1 → обрезка: [:-2] → "" + "..." → "..."
    ]
)
def test_helper_parametrized(input_msg, max_len, expected):
    assert helper(input_msg, max_length=max_len) == expected


# test_file.py
def test_read_file(temp_file):  # ← имя аргумента = имя фикстуры
    # Проверяем, что файл существует и содержит данные
    with open(temp_file, "r") as f:
        assert f.read() == "test data"