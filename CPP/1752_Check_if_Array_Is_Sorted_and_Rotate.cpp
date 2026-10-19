// 19/10/2026
// Easy
// LeetCode 1752: Check if Array Is Sorted and Rotated using O(N) cyclic modulo counting.

#include <vector>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }
        return count <= 1;
    }
};

// Local testing driver
#include <iostream>
int main() {
    Solution sol;
    std::vector<int> ex1 = {3, 4, 5, 1, 2};
    std::vector<int> ex2 = {2, 1, 3, 4};
    std::vector<int> ex3 = {1, 2, 3};
    std::cout << std::boolalpha << sol.check(ex1) << "\n";
    std::cout << std::boolalpha << sol.check(ex2) << "\n";
    std::cout << std::boolalpha << sol.check(ex3) << "\n";
    return 0;
}