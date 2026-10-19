// 19/10/2026
// Easy
// LeetCode 2089: Find Target Indices After Sorting Array using O(N) frequency counting.

#include <vector>

class Solution {
public:
    std::vector<int> targetIndices(std::vector<int>& nums, int target) {
        int less_count = 0;
        int target_count = 0;
        
        for (int num : nums) {
            if (num < target) {
                less_count++;
            } else if (num == target) {
                target_count++;
            }
        }
        
        std::vector<int> result;
        result.reserve(target_count);
        for (int i = 0; i < target_count; ++i) {
            result.push_back(less_count + i);
        }
        
        return result;
    }
};