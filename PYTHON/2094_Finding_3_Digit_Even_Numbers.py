# 21/09/2026
# Easy
# LeetCode 2094: Finding 3-Digit Even Numbers using frequency counting and space inversion.

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        count = [0] * 10
        for d in digits:
            count[d] += 1   
        res = []
        for i in range(100, 1000, 2):
            req = [0] * 10
            req[i // 100] += 1
            req[(i // 10) % 10] += 1
            req[i % 10] += 1      
            valid = True
            for j in range(10):
                if req[j] > count[j]:
                    valid = False
                    break
            if valid:
                res.append(i)     
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.findEvenNumbers([2, 1, 3, 0]))
    print(sol.findEvenNumbers([2, 2, 8, 8, 2]))
    print(sol.findEvenNumbers([3, 7, 5]))