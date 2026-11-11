// 11/11/2026
// Medium
// Generate valid IP addresses by using backtracking to segment a digit string

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> restoreIpAddresses(std::string s) {
        std::vector<std::string> result;
        std::string current_ip;
        
        auto backtrack = [&](auto& self, int start_index, int part_count) -> void {
            if (part_count == 4 && start_index == s.length()) {
                result.push_back(current_ip.substr(0, current_ip.length() - 1));
                return;
            }
            if (part_count == 4 || start_index == s.length()) {
                return;
            }
            
            for (int len = 1; len <= 3 && start_index + len <= s.length(); ++len) {
                std::string part = s.substr(start_index, len);
                
                if (part.length() > 1 && part[0] == '0') continue;
                if (std::stoi(part) > 255) continue;
                
                int original_len = current_ip.length();
                current_ip += part + ".";
                
                self(self, start_index + len, part_count + 1);
                
                current_ip.erase(original_len);
            }
        };
        
        backtrack(backtrack, 0, 0);
        return result;
    }
};