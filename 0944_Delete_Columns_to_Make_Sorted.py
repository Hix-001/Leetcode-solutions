# 30/08/2026
# Easy
# LeetCode 944: Delete Columns to Make Sorted using column-first traversal.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deleted_count = 0
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        for col in range(num_cols):
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    deleted_count += 1
                    break
                    
        return deleted_count