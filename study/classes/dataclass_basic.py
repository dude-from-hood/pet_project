from dataclasses import dataclass, asdict

"""
dataclass` автоматически создает `__init__`, `__repr__`, `__eq__` и другие методы.
"""


@dataclass
class Dog:
    name: str
    age: int


# Все! Всё остальное @dataclass сделала за нас.
my_dog = Dog("Рекс", 5)
print(my_dog)  # Dog(name='Рекс', age=5)

# перевод в словарь через спец.метод asdict()
dog_dict = asdict(my_dog)
print(dog_dict) # {'name': 'Рекс', 'age': 5}

