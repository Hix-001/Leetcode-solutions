// 25/10/2026
// Medium
// LeetCode 1254: Number of Closed Islands using boundary elimination DFS.

#include <vector>

class Solution {
public:
int closedIsland(std::vector<std::vector<int>>& grid) {
    int rows = grid.size();
    if (rows == 0) return 0;
    int cols = grid[0].size();

    auto dfs = [&](auto& self, int r, int c) -> void {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 1) {
            return;
        }
        grid[r][c] = 1; 
        self(self, r + 1, c);
        self(self, r - 1, c);
        self(self, r, c + 1);
        self(self, r, c - 1);
    };

    for (int i = 0; i < rows; ++i) {
        if (grid[i][0] == 0) dfs(dfs, i, 0);
        if (grid[i][cols - 1] == 0) dfs(dfs, i, cols - 1);
    }
    for (int j = 0; j < cols; ++j) {
        if (grid[0][j] == 0) dfs(dfs, 0, j);
        if (grid[rows - 1][j] == 0) dfs(dfs, rows - 1, j);
    }

    int count = 0;
    for (int i = 1; i < rows - 1; ++i) {
        for (int j = 1; j < cols - 1; ++j) {
            if (grid[i][j] == 0) {
                dfs(dfs, i, j);
                count++;
            }
        }
    }

    return count;
}
};
