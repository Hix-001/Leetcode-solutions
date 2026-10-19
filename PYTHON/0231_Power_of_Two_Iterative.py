# 13/08/2026
# Easy
# LeetCode 231: Power of Two using the iterative division method.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

#using bin() counting
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1