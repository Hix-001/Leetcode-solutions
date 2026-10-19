# 13/09/2026
# Medium
# LeetCode 318: Maximum Product of Word Lengths using bitmask character mapping.

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - 97)
            masks.append(mask)
        max_prod = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    prod = len(words[i]) * len(words[j])
                    if prod > max_prod:
                        max_prod = prod              
        return max_prod
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(sol.maxProduct(["a", "aa", "aaa", "aaaa"]))