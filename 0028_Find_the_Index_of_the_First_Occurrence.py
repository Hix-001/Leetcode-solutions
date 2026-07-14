#13/07/2026
#Easy
# LeetCode 28: Find the Index of the First Occurrence in a String using a basic sliding window and string slicing.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        if needle_len > haystack_len:
            return -1
        for i in range(haystack_len - needle_len + 1):
            current_slice = haystack[i : i + needle_len]
            if current_slice == needle:
                return i
        return -1