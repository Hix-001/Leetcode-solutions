// 23/10/2026
// Medium
// LeetCode 3644: Maximum K to Sort a Permutation using O(N) bitwise AND accumulation.

#include <vector>

class Solution {
public:
    int sortPermutation(std::vector<int>& nums) {
        int k = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != i) {
                if (k == -1) {
                    k = nums[i];
                } else {
                    k &= nums[i];
                }
            }
        }
        return k == -1 ? 0 : k;
    }
};