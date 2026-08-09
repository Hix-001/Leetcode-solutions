# 09/08/2026
# Medium
# LeetCode 53: Maximum Subarray using Kadane's algorithm.
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
            
        return max_sum