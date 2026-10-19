#20/07/2026
#Medium
# LeetCode 11: Container With Most Water using a basic two-pointer approach to maximize area.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            current_width = right - left
            
            if height[left] < height[right]:
                current_height = height[left]
                left += 1
            else:
                current_height = height[right]
                right -= 1
                
            current_area = current_width * current_height
            
            if current_area > max_area:
                max_area = current_area
                
        return max_area
