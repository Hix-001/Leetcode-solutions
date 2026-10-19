# 11/09/2026
# Easy
# LeetCode 2085: Count Common Words With One Occurrence using basic dictionary frequency maps.

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        freq1 = {}
        for word in words1:
            if word in freq1:
                freq1[word] += 1
            else:
                freq1[word] = 1
                
        freq2 = {}
        for word in words2:
            if word in freq2:
                freq2[word] += 1
            else:
                freq2[word] = 1
                
        count = 0
        for word in freq1:
            if freq1[word] == 1 and word in freq2 and freq2[word] == 1:
                count += 1
                
        return count