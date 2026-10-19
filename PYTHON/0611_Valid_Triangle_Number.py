# 08/09/2026
# Medium
# LeetCode 611: Valid Triangle Number using sorting and two pointers.

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
                    
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.triangleNumber([2, 2, 3, 4]))
    print(sol.triangleNumber([4, 2, 3, 4]))