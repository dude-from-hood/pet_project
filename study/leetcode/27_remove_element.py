from typing import List

if __name__ == '__main__':

    """
    Вход: nums = [0,1,2,2,3,0,4,2], val = 2
    Выход: 5, nums = [0,1,3,0,4,_,_,_]
    
    Решение
     ввести 2 указателя:
     i — это "указатель записи",
     j — "указатель чтения".
     
    Фильтруем массив, перезаписывая нужные элементы подряд.
    """

    numbers = [0, 1, 2, 2, 3, 0, 4, 2]
    num = 2


    class Solution:
        def removeElement(self, nums: List[int], val: int) -> tuple:
            i = 0
            for j in range(len(nums)):
                if nums[j] != val:
                    nums[i] = nums[j]  # модифицируем массив, собирая элементы != val в начале.
                    i += 1

            # Заполняем хвост '_' это уже для красоты
            for k in range(i, len(nums)):
                nums[k] = '_'

            return i, nums

        """ 
        важный момент на строке 26:
        мы это делаем тк есть условие в задаче чтобы первые k элементы содержали все элементы ≠ val (в любом порядке).
        """


    s = Solution()
    result = s.removeElement(nums=numbers, val=num)
    print(result)
