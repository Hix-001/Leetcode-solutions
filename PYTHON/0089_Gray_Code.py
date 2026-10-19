# 24/09/2026
# Medium
# LeetCode 89: Gray Code using iterative reflection and bitwise masking.

class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]
        for i in range(n):
            mask = 1 << i
            length = len(res)
            for j in range(length - 1, -1, -1):
                res.append(res[j] + mask)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2))
    print(sol.grayCode(1))