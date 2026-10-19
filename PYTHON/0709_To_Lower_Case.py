# 03/09/2026
# Easy
# LeetCode 709: To Lower Case using ASCII mathematical offset.

class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for char in s:
            if 'A' <= char <= 'Z':
                res += chr(ord(char) + 32)
            else:
                res += char
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("Hello"))
    print(sol.toLowerCase("here"))
    print(sol.toLowerCase("LOVELY"))