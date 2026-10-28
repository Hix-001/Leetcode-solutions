// 28/10/2026
// Medium
// LeetCode 3882: Minimum XOR Path in a Grid using multi-state adaptive DP.

#include <vector>
#include <algorithm>

class Solution {
public:
    int minCost(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::vector<std::vector<int>> dp(n);
        dp[0] = {grid[0][0]};
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                std::vector<int> curr;
                if (i > 0) {
                    for (int v : dp[j]) {
                        curr.push_back(v ^ grid[i][j]);
                    }
                }
                if (j > 0) {
                    for (int v : dp[j-1]) {
                        curr.push_back(v ^ grid[i][j]);
                    }
                }
                std::sort(curr.begin(), curr.end());
                curr.erase(std::unique(curr.begin(), curr.end()), curr.end());
                dp[j] = std::move(curr);
            }
        }
        return dp[n-1].empty() ? 0 : dp[n-1][0];
    }
};