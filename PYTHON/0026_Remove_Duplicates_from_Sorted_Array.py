#15/07/2026
#Easy
# LeetCode 26: Remove Duplicates from Sorted Array using a basic reader and writer pointer.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
            
        writer = 1
        
        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1
                
        return writer