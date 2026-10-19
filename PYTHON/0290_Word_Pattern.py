# 28/07/2026
# Easy
# LeetCode 290: Word Pattern using a hash map and set to ensure strict 1-to-1 bijection.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        mapped_words = set()
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in mapped_words:
                    return False
                char_to_word[char] = word
                mapped_words.add(word)
                
        return True