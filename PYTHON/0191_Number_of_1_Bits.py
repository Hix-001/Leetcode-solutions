#10/07/2026
#Easy
# LeetCode 191: Calculate the Hamming weight of an integer using Brian Kernighan's Algorithm.
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count