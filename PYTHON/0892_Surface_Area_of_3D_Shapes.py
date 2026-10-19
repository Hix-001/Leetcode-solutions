# 28/08/2026
# Easy
# LeetCode 892: Surface Area of 3D Shapes

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        res = 0
        n = len(grid)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    res += (grid[r][c] * 4) + 2
                    
                if r > 0:
                    res -= min(grid[r][c], grid[r - 1][c]) * 2
                    
                if c > 0:
                    res -= min(grid[r][c], grid[r][c - 1]) * 2
                    
        return res