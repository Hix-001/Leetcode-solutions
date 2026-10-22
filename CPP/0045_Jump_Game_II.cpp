// 22/10/2026
// Medium
// LeetCode 45: Jump Game II using O(N) greedy implicit BFS.

#include <vector>
#include <algorithm>

class Solution {
public:
    int jump(std::vector<int>& nums) {
        int jumps = 0;
        int current_end = 0;
        int farthest = 0;
        int n = nums.size();
        
        for (int i = 0; i < n - 1; ++i) {
            farthest = std::max(farthest, i + nums[i]);
            if (i == current_end) {
                jumps++;
                current_end = farthest;
            }
        }
        
        return jumps;
    }
};