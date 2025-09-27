"""
https://leetcode.com/problems/climbing-stairs/

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1  # f(1)
    prev1 = 2  # f(2)

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

# Примеры:
print(climbStairs(5))  # Output: 8
print(climbStairs(6))  # Output: 13
