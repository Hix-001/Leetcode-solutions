# 06/09/2026
# Easy
# LeetCode 884: Uncommon Words from Two Sentences using a combined frequency map.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        combined = s1 + " " + s2
        words = combined.split()
        
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
                
        res = []
        for word in counts:
            if counts[word] == 1:
                res.append(word)
                
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))
    print(sol.uncommonFromSentences("apple apple", "banana"))