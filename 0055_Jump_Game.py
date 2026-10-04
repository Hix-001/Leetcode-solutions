# 04/10/2026
# Medium
# LeetCode 55: Jump Game using a backward greedy goalpost shift.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i                
        return goal == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))
    print(sol.canJump([3, 2, 1, 0, 4]))