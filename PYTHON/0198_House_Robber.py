# 01/10/2026
# Medium
# LeetCode 198: House Robber using space-optimized 1D Dynamic Programming.

class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0        
        for num in nums:
            temp = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = temp            
        return prev1
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))