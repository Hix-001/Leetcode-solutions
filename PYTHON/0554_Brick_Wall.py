# 11/09/2026
# Medium
# LeetCode 554: Brick Wall using prefix sums and edge frequency counting.

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edge_freq = {}
        max_edges = 0
        
        for row in wall:
            pos = 0
            for i in range(len(row) - 1):
                pos += row[i]
                if pos in edge_freq:
                    edge_freq[pos] += 1
                else:
                    edge_freq[pos] = 1
                
                if edge_freq[pos] > max_edges:
                    max_edges = edge_freq[pos]
                    
        return len(wall) - max_edges

if __name__ == "__main__":
    sol = Solution()
    print(sol.leastBricks([[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]))
    print(sol.leastBricks([[1], [1], [1]]))