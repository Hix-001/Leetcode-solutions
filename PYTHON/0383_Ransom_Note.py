# 21/08/2026
# Easy
# LeetCode 383: Ransom Note using frequency counting.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True