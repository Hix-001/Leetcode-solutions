# 29/09/2026
# Medium
# LeetCode 162: Find Peak Element using O(log n) binary search slope detection.

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))