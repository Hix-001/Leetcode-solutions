# 07/10/2026
# Hard
# LeetCode 301: Remove Invalid Parentheses using Level-Order BFS and Set deduplication.

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            level = next_level
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
    print(sol.removeInvalidParentheses("(a)())()"))
    print(sol.removeInvalidParentheses(")("))