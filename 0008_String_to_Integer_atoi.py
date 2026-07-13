#12/07/2026
#Medium
# LeetCode 8: Convert a string to an integer (atoi) using sequential pointer parsing.

class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result *= sign
        INT_MIN, INT_MAX = -2147483648, 2147483647
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        return result