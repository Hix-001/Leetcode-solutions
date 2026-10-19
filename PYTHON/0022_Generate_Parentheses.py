# 26/07/2026
# Medium
# LeetCode 22: Generate Parentheses using Backtracking by maintaining open and closed parenthesis counts.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(open_count: int, closed_count: int, path: str):
            if open_count == n and closed_count == n:
                res.append(path)
                return
            if open_count < n:
                backtrack(open_count + 1, closed_count, path + "(")
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, path + ")")
        backtrack(0, 0, "")
        return res