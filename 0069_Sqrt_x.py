#21/07/2026
#Easy
# LeetCode 69: Sqrt(x) using basic Binary Search on the range of possible answers.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
            
        left = 1
        right = x // 2
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
                
        return result