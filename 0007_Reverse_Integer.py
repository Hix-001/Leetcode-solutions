#08/07/2026
#Medium
# LeetCode 7: Reverse a 32-bit integer using optimized string slicing and bounds checking.
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            rev = int('-' + s[1:][::-1])
        else:
            rev = int(s[::-1])
        return rev if -2147483648 <= rev <= 2147483647 else 0
    
#OR

class Solution:
    def reverse(self, x: int) -> int:
        rev = -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        return rev if -2147483648 <= rev <= 2147483647 else 0