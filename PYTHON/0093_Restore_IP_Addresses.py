# 25/09/2026
# Medium
# LeetCode 93: Restore IP Addresses using constraint-based backtracking.

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) < 4 or len(s) > 12:
            return res
        def backtrack(i, path):
            if len(path) == 4:
                if i == len(s):
                    res.append(".".join(path))
                return
            for j in range(i + 1, min(i + 4, len(s) + 1)):
                segment = s[i:j]
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                backtrack(j, path + [segment]) 
        backtrack(0, [])
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("0000"))
    print(sol.restoreIpAddresses("101023"))