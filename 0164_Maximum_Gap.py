# 07/09/2026
# Medium
# LeetCode 164: Maximum Gap using linear-time Bucket Sort.

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
            
        min_val = min(nums)
        max_val = max(nums)
        
        if min_val == max_val:
            return 0
            
        n = len(nums)
        gap = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // gap + 1
        
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [-1] * bucket_count
        
        for num in nums:
            idx = (num - min_val) // gap
            if num < bucket_min[idx]:
                bucket_min[idx] = num
            if num > bucket_max[idx]:
                bucket_max[idx] = num
                
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            if bucket_max[i] == -1:
                continue
            if bucket_min[i] - prev_max > max_gap:
                max_gap = bucket_min[i] - prev_max
            prev_max = bucket_max[i]
            
        return max_gap

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumGap([3, 6, 9, 1]))
    print(sol.maximumGap([10]))