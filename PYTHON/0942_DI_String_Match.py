# 30/08/2026
# Easy
# LeetCode 942: DI String Match using greedy two pointers.

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low = 0
        high = len(s)
        res = []
        
        for char in s:
            if char == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
                
        res.append(low)
        return res