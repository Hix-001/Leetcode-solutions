# 26/07/2026
# Easy
# LeetCode 136: Single Number using bitwise XOR to cancel out paired elements.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result