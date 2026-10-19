# 09/09/2026
# Medium
# LeetCode 442: Find All Duplicates in an Array using O(1) space sign marking.

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    print(sol.findDuplicates([1, 1, 2]))
    print(sol.findDuplicates([1]))