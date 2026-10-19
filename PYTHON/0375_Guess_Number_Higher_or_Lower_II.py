# 30/09/2026
# Medium
# LeetCode 375: Guess Number Higher or Lower II using Interval DP and Minimax.

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                min_cost = float('inf')
                for k in range(i, j + 1):
                    worst_case_for_k = k + max(dp[i][k - 1], dp[k + 1][j])
                    min_cost = min(min_cost, worst_case_for_k)
                dp[i][j] = min_cost
        return dp[1][n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.getMoneyAmount(10))
    print(sol.getMoneyAmount(1))
    print(sol.getMoneyAmount(2))