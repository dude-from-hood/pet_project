from typing import List

"""
Example:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Ключевые моменты:
Вводим 2 индекса/указателя = i, j
Один (i) будет указывать на текущую позицию, куда нужно записать уникальный элемент.
Второй (j) будет пробегать по списку в поисках нового уникального элемента.

i — указывает на конец уникальной части.
j — ищет новые уникальные элементы.

После цикла заполняем хвост '_'.

Мы сканируем уникальную часть на уникальные элементы.
"""



# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#
# if not nums:
#     print(0, nums)
# else:
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#
#     # Заполняем хвост '_'
#     for k in range(i + 1, len(nums)):
#         nums[k] = '_'
#
#     print(i + 1, nums)


def upd_dict(*args, **kwargs):
    s = dict()

    # Обрабатываем args (например, добавляем их как ключи с None-значениями)
    for i, arg in enumerate(args):
        s[f"arg_{i}"] = arg

    s.update(kwargs)

    return s

print(upd_dict('sdr', a=1, b=2, c=3, d=4))
