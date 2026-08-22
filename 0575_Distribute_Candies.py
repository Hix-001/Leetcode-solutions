# 22/08/2026
# Easy
# LeetCode 575: Distribute Candies by comparing set length and array half.

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)