# 28/09/2026
# Medium
# LeetCode 443: String Compression using two pointers for O(1) space in-place modification.

class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            while read < n and chars[read] == char:
                read += 1
                count += 1
                
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write

if __name__ == "__main__":
    sol = Solution()
    
    chars1 = ["a","a","b","b","c","c","c"]
    length1 = sol.compress(chars1)
    print(length1, chars1[:length1])
    
    chars2 = ["a"]
    length2 = sol.compress(chars2)
    print(length2, chars2[:length2])
    
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    length3 = sol.compress(chars3)
    print(length3, chars3[:length3])