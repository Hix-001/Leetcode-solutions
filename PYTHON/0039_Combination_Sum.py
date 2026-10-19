# 30/08/2026
# Medium
# LeetCode 39: Combination Sum using unlimited element backtracking.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, current_sum, current_comb):
            if current_sum == target:
                res.append(list(current_comb))
                return
            if current_sum > target:
                return
                
            for i in range(start, len(candidates)):
                current_comb.append(candidates[i])
                backtrack(i, current_sum + candidates[i], current_comb)
                current_comb.pop()
                
        backtrack(0, 0, [])
        return res