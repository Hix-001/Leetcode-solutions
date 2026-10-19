# 09/09/2026
# Medium
# LeetCode 139: Word Break using 1D Dynamic Programming.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word:
                    if dp[i - len(word)]:
                        dp[i] = True
                        break
                        
        return dp[len(s)]
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))