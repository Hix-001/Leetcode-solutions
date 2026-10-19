# 20/08/2026
# Easy
# LeetCode 1160: Find Words That Can Be Formed by Characters using Hash Maps.

from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            good = True
            
            for char, count in word_count.items():
                if chars_count[char] < count:
                    good = False
                    break
                    
            if good:
                total_length += len(word)
                
        return total_length