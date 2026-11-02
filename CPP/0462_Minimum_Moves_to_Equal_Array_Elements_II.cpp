// 02/11/2026
// Medium
// Calculate minimum moves by finding the median using nth_element and summing absolute differences
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int minMoves2(std::vector<int>& nums) {
        int n = nums.size();
        std::nth_element(nums.begin(), nums.begin() + n / 2, nums.end());
        int median = nums[n / 2];
        
        long long moves = 0;
        for (int num : nums) {
            moves += std::abs(num - median);
        }
        
        return moves;
    }
};