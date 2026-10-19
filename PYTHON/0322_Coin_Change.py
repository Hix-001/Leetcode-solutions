# 13/09/2026
# Medium
# LeetCode 322: Coin Change using bottom-up 1D dynamic programming.

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))
    print(sol.coinChange([2], 3))
    print(sol.coinChange([1], 0))