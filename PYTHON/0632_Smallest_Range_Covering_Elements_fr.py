# 16/08/2026
# Hard
# LeetCode 632: Smallest Range Covering Elements from K Lists using a Min-Heap.

import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        current_max = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
            
        best_range = [-100000, 100000]
        
        while heap:
            current_min, list_idx, element_idx = heapq.heappop(heap)
            
            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]
            elif current_max - current_min == best_range[1] - best_range[0] and current_min < best_range[0]:
                best_range = [current_min, current_max]
                
            if element_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][element_idx + 1]
                heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
                current_max = max(current_max, next_val)
            else:
                break
                
        return best_range