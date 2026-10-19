# 08/08/2026
# Easy
# LeetCode 561: Array Partition using a greedy sorting approach.
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i]
        return max_sum