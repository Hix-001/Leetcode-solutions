# 29/08/2026
# Easy
# LeetCode 387: First Unique Character in a String using frequency map.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1