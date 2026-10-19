# 05/09/2026
# Easy
# LeetCode 509: Fibonacci Number using space-optimized iteration.

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        a = 0
        b = 1
        
        for _ in range(2, n + 1):
            temp = a + b
            a = b
            b = temp
            
        return b

if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))
    print(sol.fib(3))
    print(sol.fib(4))