// 22/10/2026
// Medium
// LeetCode 3942: Minimum Operations to Sort a Permutation using O(N) abstract state BFS.

#include <vector>
#include <queue>
#include <utility>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        
        int pos = -1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                pos = i;
                break;
            }
        }
        
        bool is_forward = true;
        for (int i = 0; i < n; ++i) {
            if (nums[(pos + i) % n] != i) {
                is_forward = false;
                break;
            }
        }
        
        bool is_backward = true;
        for (int i = 0; i < n; ++i) {
            if (nums[(pos - i + n) % n] != i) {
                is_backward = false;
                break;
            }
        }
        
        if (!is_forward && !is_backward) {
            return -1;
        }
        
        std::vector<std::vector<int>> dist(n, std::vector<int>(2, -1));
        std::queue<std::pair<int, int>> q;
        
        if (is_forward) {
            q.push({pos, 0});
            dist[pos][0] = 0;
        }
        if (is_backward) {
            q.push({pos, 1});
            dist[pos][1] = 0;
        }
        
        while (!q.empty()) {
            auto [p, d] = q.front();
            q.pop();
            
            if (p == 0 && d == 0) {
                return dist[p][d];
            }
            
            int np1 = (p - 1 + n) % n;
            if (dist[np1][d] == -1) {
                dist[np1][d] = dist[p][d] + 1;
                q.push({np1, d});
            }
            
            int np2 = n - 1 - p;
            int nd2 = 1 - d;
            if (dist[np2][nd2] == -1) {
                dist[np2][nd2] = dist[p][d] + 1;
                q.push({np2, nd2});
            }
        }
        
        return -1;
    }
};