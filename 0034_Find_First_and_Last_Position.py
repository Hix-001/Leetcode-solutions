#16/07/2026
#Medium
# LeetCode 34: Find First and Last Position of Element in Sorted Array using two modified Binary Searches.
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def find_bound(is_first: bool) -> int:
            left = 0
            right = len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    result = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
            return result

        start_index = find_bound(True)
        end_index = find_bound(False)
        
        return [start_index, end_index]