// 10/11/2026
// Medium
// Sort an array of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm

#include <vector>
#include <utility>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                std::swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                std::swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};