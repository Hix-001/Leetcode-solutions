// 01/11/2026
// Medium
// Calculate minimum moves to equalize array by modeling n-1 increments as single decrements

#include <vector>
#include <algorithm>

class Solution {
public:
    int minMoves(std::vector<int>& nums) {
        int min_val = *std::min_element(nums.begin(), nums.end());
        int moves = 0;
        for (int num : nums) {
            moves += (num - min_val);
        }
        return moves;
    }
};