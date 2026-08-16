# 14/08/2026
# Easy
# LeetCode 461: Hamming Distance using basic bitwise XOR and shifting.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        distance = 0
        
        while xor_result > 0:
            distance += xor_result & 1
            xor_result >>= 1
            
        return distance
    