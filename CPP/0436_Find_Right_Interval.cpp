// 14/11/2026
// Medium
// Find right intervals using sorting and binary search (lower_bound) on start times

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> findRightInterval(std::vector<std::vector<int>>& intervals) {
        int n = intervals.size();
        std::vector<std::pair<int, int>> start_indices;
        start_indices.reserve(n);
        
        for (int i = 0; i < n; ++i) {
            start_indices.push_back({intervals[i][0], i});
        }
        
        std::sort(start_indices.begin(), start_indices.end());
        
        std::vector<int> result(n, -1);
        for (int i = 0; i < n; ++i) {
            int end_val = intervals[i][1];
            
            auto it = std::lower_bound(start_indices.begin(), start_indices.end(), end_val, 
                [](const std::pair<int, int>& a, int val) {
                    return a.first < val;
                });
            
            if (it != start_indices.end()) {
                result[i] = it->second;
            }
        }
        
        return result;
    }
};