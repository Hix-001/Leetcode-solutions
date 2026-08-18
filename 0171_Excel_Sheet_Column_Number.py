# 18/08/2026
# Easy
# LeetCode 171: Excel Sheet Column Number using base 26 accumulation.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            res = res * 26 + (ord(char) - ord('A') + 1)
        return res
    