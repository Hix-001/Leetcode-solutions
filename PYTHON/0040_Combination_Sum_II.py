# 30/08/2026
# Medium
# LeetCode 40: Combination Sum II using sorting and duplicate skipping.

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start, current_sum, current_comb):
            if current_sum == target:
                res.append(list(current_comb))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                if current_sum + candidates[i] > target:
                    break
                    
                current_comb.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], current_comb)
                current_comb.pop()
                
        backtrack(0, 0, [])
        return res