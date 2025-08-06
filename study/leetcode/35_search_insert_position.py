"""
Input: nums = [1,3,5,6], target = 5
Output: 2

######
Input: nums = [1,3,5,6], target = 2
Output: 1
"""
from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        if target in nums:
            pos = nums.index(target)
            return pos
        else:
            i = 0
            if target > nums[-1]:
                return nums.index(nums[-1]) + 1

            for j in range(len(nums)):
                if target > nums[j]:
                    i += 1
                    continue
                else:
                    return i


nums = list(range(1, 20, 2))
print(nums)
target = 6

s = Solution()

print(s.search_insert(nums=nums, target=target))
