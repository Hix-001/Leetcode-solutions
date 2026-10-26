// 26/10/2026
// Medium
// LeetCode 3619: Count Islands With Total Value Divisible by K using modulo DFS Flood Fill.

#include <vector>

class Solution {
public:
    int countIslands(std::vector<std::vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;

        auto dfs = [&](auto& self, int r, int c) -> long long {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
                return 0;
            }
            long long val = grid[r][c] % k;
            grid[r][c] = 0;
            
            val = (val + self(self, r + 1, c)) % k;
            val = (val + self(self, r - 1, c)) % k;
            val = (val + self(self, r, c + 1)) % k;
            val = (val + self(self, r, c - 1)) % k;
            
            return val;
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0) {
                    if (dfs(dfs, i, j) == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};