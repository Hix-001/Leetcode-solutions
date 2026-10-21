// 21/10/2026
// Medium
// LeetCode 3863: Minimum Operations to Sort a String using O(N) boundary analysis.

#include <string>
#include <algorithm>

class Solution {
public:
    int minOperations(std::string s) {
        int n = s.size();
        if (std::is_sorted(s.begin(), s.end())) {
            return 0;
        }
        if (n <= 2) {
            return -1;
        }

        char min_ch = s[0];
        char max_ch = s[0];
        for (char c : s) {
            min_ch = std::min(min_ch, c);
            max_ch = std::max(max_ch, c);
        }

        if (s[0] == min_ch || s[n - 1] == max_ch) {
            return 1;
        }

        bool has_min_not_at_end = false;
        bool has_max_not_at_start = false;

        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == min_ch) {
                has_min_not_at_end = true;
                break;
            }
        }

        for (int i = 1; i < n; ++i) {
            if (s[i] == max_ch) {
                has_max_not_at_start = true;
                break;
            }
        }

        if (has_min_not_at_end || has_max_not_at_start) {
            return 2;
        }

        return 3;
    }
};