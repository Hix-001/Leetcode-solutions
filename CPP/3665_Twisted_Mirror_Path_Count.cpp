// 31/10/2026
// Medium
// LeetCode 3665: Twisted Mirror Path Count using abstract ray-tracing simulation and DAG DP.

#include <vector>

class Solution {
public:
    int uniquePaths(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int MOD = 1e9 + 7;
        
        std::vector<std::vector<std::vector<int>>> memo_ray(m, std::vector<std::vector<int>>(n, std::vector<int>(2, -2)));
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, -1));
        
        auto get_dest = [&](auto& self, int r, int c, int dir) -> int {
            if (r >= m || c >= n) return -1;
            if (grid[r][c] == 0) return r * n + c;
            
            if (memo_ray[r][c][dir] != -2) {
                return memo_ray[r][c][dir];
            }
            
            int res;
            if (dir == 0) { 
                res = self(self, r + 1, c, 1);
            } else { 
                res = self(self, r, c + 1, 0);
            }
            
            return memo_ray[r][c][dir] = res;
        };
        
        auto dfs = [&](auto& self, int r, int c) -> int {
            if (r == m - 1 && c == n - 1) return 1;
            if (dp[r][c] != -1) return dp[r][c];
            
            long long ways = 0;
            
            int d_right = get_dest(get_dest, r, c + 1, 0);
            if (d_right != -1) {
                ways = (ways + self(self, d_right / n, d_right % n)) % MOD;
            }
            
            int d_down = get_dest(get_dest, r + 1, c, 1);
            if (d_down != -1) {
                ways = (ways + self(self, d_down / n, d_down % n)) % MOD;
            }
            
            return dp[r][c] = ways;
        };
        
        return dfs(dfs, 0, 0);
    }
};