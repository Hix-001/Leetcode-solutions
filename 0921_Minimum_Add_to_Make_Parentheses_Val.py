# 06/10/2026
# Medium
# LeetCode 921: Minimum Add to Make Parentheses Valid using O(1) space state tracking.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0        
        for char in s:
            if char == '(':
                close_needed += 1
            elif char == ')':
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1                    
        return open_needed + close_needed
if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))