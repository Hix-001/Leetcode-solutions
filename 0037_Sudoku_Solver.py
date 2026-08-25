# 25/08/2026
# Hard
# LeetCode 37: Sudoku Solver using Backtracking.
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
        def backtrack(idx):
            if idx == len(empty_cells):
                return True
                
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for k in "123456789":
                if k not in rows[r] and k not in cols[c] and k not in boxes[box_idx]:
                    board[r][c] = k
                    rows[r].add(k)
                    cols[c].add(k)
                    boxes[box_idx].add(k)
                    
                    if backtrack(idx + 1):
                        return True
                        
                    board[r][c] = '.'
                    rows[r].remove(k)
                    cols[c].remove(k)
                    boxes[box_idx].remove(k)
                    
            return False
            
        backtrack(0)