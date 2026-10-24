// 24/10/2026
// Easy
// LeetCode 2409: Count Days Spent Together using day-of-year scalar conversion and interval intersection.

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int countDaysTogether(std::string arriveAlice, std::string leaveAlice, std::string arriveBob, std::string leaveBob) {
        auto toDayOfYear = [](const std::string& date) {
            std::vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            int month = std::stoi(date.substr(0, 2));
            int day = std::stoi(date.substr(3, 2));
            int totalDays = 0;
            for (int i = 0; i < month - 1; ++i) {
                totalDays += daysInMonth[i];
            }
            totalDays += day;
            return totalDays;
        };

        int aStart = toDayOfYear(arriveAlice);
        int aEnd = toDayOfYear(leaveAlice);
        int bStart = toDayOfYear(arriveBob);
        int bEnd = toDayOfYear(leaveBob);

        int start = std::max(aStart, bStart);
        int end = std::min(aEnd, bEnd);

        return std::max(0, end - start + 1);
    }
};