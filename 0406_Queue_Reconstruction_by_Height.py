# 19/09/2026
# Medium
# LeetCode 406: Queue Reconstruction by Height using Greedy insertion.

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)     
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(sol.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))