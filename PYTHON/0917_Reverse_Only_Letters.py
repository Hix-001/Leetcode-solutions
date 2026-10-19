# 06/09/2026
# Easy
# LeetCode 917: Reverse Only Letters using two pointers and string mutability.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(chars) - 1
        
        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left += 1
                right -= 1
                
        return "".join(chars)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseOnlyLetters("ab-cd"))
    print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))