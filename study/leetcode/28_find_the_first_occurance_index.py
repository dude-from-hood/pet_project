

"""
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Найти индекс первого вхождения подстроки в строке.
"""


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
sol = Solution()

print(sol.str_str(haystack, needle))

