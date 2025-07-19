from collections import Counter

"""
Уже знакомый вам класс для подсчёта хешируемых объектов.
Методы:

elements() — итератор по элементам (с повторениями).

most_common(n) — n самых частых элементов.

subtract() — вычитание счетчиков.

Арифметические операции (+, -, &, |).
"""

c = Counter("abracadabra")
print(c.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]

from collections import defaultdict

dd = defaultdict(list)
dd["fruits"].append("apple")  # Не нужно проверять наличие ключа!
print(dd)

from collections import deque

"""
Двусторонняя очередь. Быстрые операции (O(1)) с начала и конца.

Методы:
appendleft(), popleft() — добавление/удаление слева.
rotate(n) — циклический сдвиг на n элементов.
"""

d = deque([1, 2, 3])
d.appendleft(0)  # deque([0, 1, 2, 3])
print(d)
d.rotate(2)
print(d)

from collections import namedtuple

"""
Создаёт кортеж с именованными полями. Удобен для чтения кода.
"""
Point = namedtuple("Point", ["x", "y"])
print(Point)
p = Point(10, y=20)
print(p)
print(p.x, p.y)  # 10 20

from collections import ChainMap

"""
Объединяет несколько словарей в один интерфейс. Поиск происходит последовательно в каждом словаре.
"""

dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}
chain = ChainMap(dict1, dict2, dict3)
print(chain["c"])  # 3 (из dict3)
