# 18/09/2026
# Medium
# LeetCode 365: Water and Jug Problem using Bezout's Identity and GCD.

import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if x == 0 or y == 0:
            return target == x or target == y
        return target % math.gcd(x, y) == 0