# 01/08/2026
# Medium
# LeetCode 77: Combinations using basic backtracking.
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def backtrack(start: int, current_combo: list[int]):
            if len(current_combo) == k:
                res.append(current_combo.copy())
                return
            for i in range(start, n + 1):
                current_combo.append(i)
                backtrack(i + 1, current_combo)
                current_combo.pop()
        backtrack(1, [])
        return res