#10/07/2026
#Easy
# LeetCode 20: Determine if a string of brackets is valid using a Stack and Hash Map mapping in O(N) time.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack