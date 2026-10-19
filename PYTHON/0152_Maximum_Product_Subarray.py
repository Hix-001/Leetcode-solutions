# 03/10/2026
# Medium
# LeetCode 152: Maximum Product Subarray using modified Kadane's algorithm with min/max bounds.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0            
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]        
        for i in range(1, len(nums)):
            n = nums[i]            
            # We must store cur_max in a temporary variable because we need 
            # the old cur_max to calculate the new cur_min.
            temp_max = max(n, cur_max * n, cur_min * n)
            cur_min = min(n, cur_max * n, cur_min * n)
            cur_max = temp_max            
            res = max(res, cur_max)            
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))
    print(sol.maxProduct([-2, 0, -1]))