// 21/10/2026
// Easy
// LeetCode 1: Two Sum using O(N) single-pass hash map complement lookup.

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_index;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int complement = target - nums[i];
            auto it = num_to_index.find(complement);
            if (it != num_to_index.end()) {
                return {it->second, i};
            }
            num_to_index[nums[i]] = i;
        }
        
        return {};
    }
};