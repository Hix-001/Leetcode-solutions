# 10/08/2026
# Easy
# LeetCode 557: Reverse Words in a String III using split, slice, and join.
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)