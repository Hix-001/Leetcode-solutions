# 26/09/2026
# Medium
# LeetCode 165: Compare Version Numbers using string splitting and integer padding.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        
        n = max(len(v1_list), len(v2_list))
        
        for i in range(n):
            num1 = int(v1_list[i]) if i < len(v1_list) else 0
            num2 = int(v2_list[i]) if i < len(v2_list) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
                
        return 0