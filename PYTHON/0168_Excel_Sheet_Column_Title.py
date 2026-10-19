# 18/08/2026
# Easy
# LeetCode 168: Excel Sheet Column Title using base-26 shifting.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            res.append(chr(remainder + ord('A')))
            columnNumber //= 26
        return "".join(reversed(res))
        