# 11/10/2026
# Medium
# LeetCode 2333: Minimum Sum of Squared Difference using O(N+M) greedy frequency mapping.

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        if sum(diffs) <= k:
            return 0
            
        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)
        for d in diffs:
            counts[d] += 1
            
        for d in range(max_diff, 0, -1):
            if counts[d] > 0:
                if k >= counts[d]:
                    counts[d - 1] += counts[d]
                    k -= counts[d]
                    counts[d] = 0
                else:
                    counts[d - 1] += k
                    counts[d] -= k
                    k = 0
                    break
                    
        ans = 0
        for d in range(1, max_diff + 1):
            if counts[d] > 0:
                ans += (d * d) * counts[d]
                
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0))
    print(sol.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1))