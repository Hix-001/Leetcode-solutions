# 04/09/2026
# Easy
# LeetCode 463: Island Perimeter using grid traversal and overlap deduction.

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                        
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                        
        return perimeter

if __name__ == "__main__":
    sol = Solution()
    print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(sol.islandPerimeter([[1]]))
    print(sol.islandPerimeter([[1,0]]))

    