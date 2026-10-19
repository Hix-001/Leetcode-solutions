# 06/09/2026
# Easy
# LeetCode 1784: Check if Binary String Has at Most One Segment of Ones

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_zero = False
        for char in s:
            if char == '0':
                found_zero = True
            elif char == '1' and found_zero:
                return False
        return True