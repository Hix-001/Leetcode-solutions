# 12/09/2026
# Medium
# LeetCode 62: Unique Paths using space-optimized dynamic programming.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))
    print(sol.uniquePaths(3, 2))