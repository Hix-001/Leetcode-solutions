#07/07/2026
# LeetCode 27: Remove all occurrences of a value in-place using a reader/writer two-pointer approach.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k