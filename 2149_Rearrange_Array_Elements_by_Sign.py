# 15/09/2026
# Medium
# LeetCode 2149: Rearrange Array Elements by Sign using independent parity pointers.

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2  
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrangeArray([3, 1, -2, -5, 2, -4]))
    print(sol.rearrangeArray([-1, 1]))