# 02/09/2026
# Easy
# LeetCode 804: Unique Morse Code Words using ASCII offset and Hash Set.

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_transformations = set()
        
        for word in words:
            current_transformation = ""
            for char in word:
                current_transformation += morse_map[ord(char) - ord('a')]
            unique_transformations.add(current_transformation)
            
        return len(unique_transformations)

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
    print(sol.uniqueMorseRepresentations(["a"]))