"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

+-------------------------------------------
Для [1, 2, 3] (длина 3) → len(digits) - 1 = 2 (это индекс последней цифры).

операцию - 1 нужно делать тк индексы начинаются с 0, значит последний индекс будет равен (длина списка - 1)
"""

def plus_one(digits: list) -> list:
    carry = 1                                   # начинаем с carry = 1, потому что нужно прибавить 1 к числу
    for i in range(len(digits) - 1, -1, -1):    # старт (с последнего индекса), стоп (на индексе -1), шаг (обратный ход)
        digits[i] += carry                      # digits[1] = 9 + 1 = 10
        carry = digits[i] // 10                 # carry = 10 // 10 = 1
        digits[i] %= 10                         # digits[1] = 10 % 10 = 0
        if carry == 0:
            break
    if carry:
        digits.insert(0, carry)
    return digits


print(plus_one([9,9]))
