# 17/09/2026
# Medium
# LeetCode 1140: Stone Game II using minimax and top-down dynamic programming.

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        s = [0] * n
        s[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] + piles[i]
        memo = {}
        def dp(i, m):
            if i + 2 * m >= n:
                return s[i]
            if (i, m) in memo:
                return memo[(i, m)]
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, s[i] - dp(i + x, max(m, x)))
            memo[(i, m)] = res
            return res
        return dp(0, 1)