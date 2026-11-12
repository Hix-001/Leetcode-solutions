// 12/11/2026
// Easy
// Find longest harmonious subsequence by counting frequencies with a hash map

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int findLHS(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        int max_len = 0;
        for (const auto& [key, val] : freq) {
            if (freq.count(key + 1)) {
                max_len = std::max(max_len, val + freq.at(key + 1));
            }
        }
        
        return max_len;
    }
};