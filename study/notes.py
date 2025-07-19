""" Файл для заметок"""
import pprint
from collections import Counter

#+---------------------------------------------
T = 1, 2, 3, 4, 5
a, b, *rest = T  # rest станет списком
#print(*T, sep=':', end="!\n")

#+---------------------------------------------


# todo: вынести в отд функцию

s = 'Hello my name is John Doe'
lst_s = list(s.lower())
dict_s = dict()
set_s = set(lst_s)

if ' ' in set_s:
    set_s.remove(" ")

for i in set_s:
    dict_s[i] = 0

for i in lst_s:
    for k, v in dict_s.items():
        if k == i:
            dict_s[k] += 1

sorted_items = sorted(dict_s.items(), key=lambda item: item[1], reverse=True)
#print(sorted_items[:2])

# +------------------------------------------
if __name__ == '__main__':

    # способ через Counter
    new_s = 'Hello my name is John Doe'

    result = dict(Counter(new_s))
    print(Counter(new_s).most_common(2))
    print(result)

    if " " in result:
        del result[" "]

    max_value = 0
    max_key = ''

    for key, value in result.items():
        if value > max_value:
            max_key, max_value = key, value

    print(f"{max_key}: {max_value}")

    # result = sorted(result.items(), key=lambda item: item[1], reverse=True)

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