// 20/10/2026
// Hard
// LeetCode 3886: Sum of Sortable Integers using O(1) drop jump pointers.

#include <vector>

class Solution {
public:
    int sortableIntegers(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> next_drop(n, n);
        int last_drop = n;
        
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]) {
                last_drop = i;
            }
            next_drop[i] = last_drop;
        }

        auto check = [&](int k) -> bool {
            int prev_max = -1;
            for (int i = 0; i < n; i += k) {
                int L = i;
                int R = i + k - 1;
                int D = next_drop[L];
                int b_min, b_max;

                if (D >= R) {
                    b_min = nums[L];
                    b_max = nums[R];
                } else {
                    if (next_drop[D + 1] < R) return false;
                    if (nums[R] > nums[L]) return false;
                    b_min = nums[D + 1];
                    b_max = nums[D];
                }

                if (b_min < prev_max) return false;
                prev_max = b_max;
            }
            return true;
        };

        int total_sum = 0;
        for (int k = 1; k * k <= n; ++k) {
            if (n % k == 0) {
                if (check(k)) total_sum += k;
                if (k * k != n) {
                    if (check(n / k)) total_sum += (n / k);
                }
            }
        }

        return total_sum;
    }
};