# 02/10/2026
# Medium
# LeetCode 498: Diagonal Traverse using boundary simulation.

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        res = []
        going_up = True
        
        for _ in range(m * n):
            res.append(mat[row][col])
            
            if going_up:
                if col == n - 1:
                    row += 1
                    going_up = False
                elif row == 0:
                    col += 1
                    going_up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    going_up = True
                elif col == 0:
                    row += 1
                    going_up = True
                else:
                    row += 1
                    col -= 1
                    
        return res