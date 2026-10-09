# 09/10/2026
# Medium
# LeetCode 1541: Minimum Insertions to Balance a Parentheses String using O(1) state tracking.

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_rights = 0
        
        for char in s:
            if char == '(':
                # If we have an odd number of needed right parentheses,
                # we must insert one ')' right now before opening a new '('
                # because the right parentheses must be consecutive.
                if needed_rights % 2 == 1:
                    insertions += 1
                    needed_rights -= 1
                
                # Every new '(' requires two '))'
                needed_rights += 2
                
            else:
                # We found one of our needed right parentheses
                needed_rights -= 1
                
                # If we have too many right parentheses (orphan ')')
                if needed_rights < 0:
                    # We must insert a '(' before it.
                    insertions += 1
                    # A new '(' needs two ')'. We just used one, so we still need one more.
                    needed_rights += 2
                    
        return insertions + needed_rights

if __name__ == "__main__":
    sol = Solution()
    print(sol.minInsertions("(()))"))
    print(sol.minInsertions("())"))
    print(sol.minInsertions("))())("))