# 29/07/2026
# Easy
# LeetCode 263: Ugly Number using repeated division by 2, 3, and 5.
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1