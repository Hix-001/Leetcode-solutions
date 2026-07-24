#23/07/2026
#Medium
# LeetCode 17: Letter Combinations of a Phone Number using Backtracking/DFS.

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, current_string: str) -> None:
            if index == len(digits):
                res.append(current_string)
                return
                
            letters = digit_to_char[digits[index]]
            for letter in letters:
                backtrack(index + 1, current_string + letter)
                
        backtrack(0, "")
        
        return res