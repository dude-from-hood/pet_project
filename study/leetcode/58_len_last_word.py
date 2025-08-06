"""
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

############
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""

s = "   fly me   to   the moon  "
last_len = len(s.split()[-1]) # разбиваем строку - удаляя пробелы - и забираем посл.элемент
print(last_len)
