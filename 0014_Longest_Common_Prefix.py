#09/10/2026
#Easy
# LeetCode 14: Find the longest common prefix by comparing lexicographical bounds in O(N*M) time.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s1 = min(strs)
        s2 = max(strs)
        
        for i, char in enumerate(s1):
            if char != s2[i]:
                return s1[:i]
                
        return s1