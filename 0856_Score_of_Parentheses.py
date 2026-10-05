# 05/10/2026
# Medium
# LeetCode 856: Score of Parentheses using O(1) mathematical depth tracking and bitwise shifts.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # If we just closed a core "()", calculate its depth multiplier
                if s[i-1] == '(':
                    score += 1 << depth                    
        return score
if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfParentheses("()"))
    print(sol.scoreOfParentheses("(())"))
    print(sol.scoreOfParentheses("()()"))