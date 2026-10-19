# 11/10/2026
# Medium
# LeetCode 2333: Minimum Sum of Squared Difference using O(N+M) greedy frequency mapping.

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(num * num for i, num in enumerate(nums, 1) if n % i == 0)