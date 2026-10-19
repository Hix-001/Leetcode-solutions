# 15/08/2026
# Medium
# LeetCode 46: Permutations using Backtracking.
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
                
        backtrack([])
        return res