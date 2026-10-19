# 19/08/2026
# Easy
# LeetCode 409: Longest Palindrome using a hash set for pairing.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        length = 0
        
        for char in s:
            if char in char_set:
                char_set.remove(char)
                length += 2
            else:
                char_set.add(char)
                
        if char_set:
            length += 1
            
        return length