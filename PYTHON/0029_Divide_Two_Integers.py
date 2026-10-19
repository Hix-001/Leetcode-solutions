# 31/08/2026
# Medium
# LeetCode 29: Divide Two Integers using bitwise shifts.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        is_negative = (dividend < 0) != (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            abs_dividend -= temp_divisor
            quotient += multiple
            
        if is_negative:
            quotient = -quotient
            
        return min(max(-2147483648, quotient), 2147483647)

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3))
    print(sol.divide(7, -3))