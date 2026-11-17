// 17/11/2026
// Easy
// Maximize stock profit by tracking the minimum price seen so far

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int min_price = 1e9; // Arbitrarily large number
        int max_profit = 0;
        
        for (int price : prices) {
            if (price < min_price) {
                min_price = price;
            } else if (price - min_price > max_profit) {
                max_profit = price - min_price;
            }
        }
        
        return max_profit;
    }
};