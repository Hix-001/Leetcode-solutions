#19/07/2026
#Hard
# LeetCode 10: Regular Expression Matching using basic Top-Down Dynamic Programming (Memoization).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
                
            if i >= len(s) and j >= len(p):
                return True
                
            if j >= len(p):
                return False
                
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                skip_star = dfs(i, j + 2)
                
                use_star = False
                if match:
                    use_star = dfs(i + 1, j)
                    
                ans = skip_star or use_star
            else:
                if match:
                    ans = dfs(i + 1, j + 1)
                else:
                    ans = False
                    
            memo[(i, j)] = ans
            return ans
            
        return dfs(0, 0)