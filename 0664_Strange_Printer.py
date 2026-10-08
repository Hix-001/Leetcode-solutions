# 08/10/2026
# Hard
# LeetCode 664: Strange Printer using O(N^3) Interval DP with string compression.

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
            
        chars = []
        for char in s:
            if not chars or chars[-1] != char:
                chars.append(char)
        s = "".join(chars)
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
                    
        return dp[0][n - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.strangePrinter("aaabbb"))
    print(sol.strangePrinter("aba"))