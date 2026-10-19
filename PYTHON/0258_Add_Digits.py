# 30/07/2026
# Easy
# LeetCode 258: Add Digits using basic loop simulation.
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            current_sum = 0
            while num > 0:
                current_sum += num % 10
                num //= 10
            num = current_sum
        return num