from common.utils.random_utils import add
def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 8
    assert add(b, a) == 8

def test_user_data(sample_user):
    assert sample_user["name"] == "Alice"
    assert sample_user["age"] == 30

def test_something():
    assert 2 + 2 == 4
