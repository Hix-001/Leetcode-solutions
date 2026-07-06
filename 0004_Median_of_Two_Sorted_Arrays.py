#hard
# LeetCode 4: Find the median of two sorted arrays using binary search on partitions in O(log(min(m,n))) time.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n
        mid_index = total_len // 2
        
        p1 = p2 = 0
        prev = curr = 0
        
        for _ in range(mid_index + 1):
            prev = curr
            
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    curr = nums1[p1]
                    p1 += 1
                else:
                    curr = nums2[p2]
                    p2 += 1
            elif p1 < m:
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
                
        if total_len % 2 == 0:
            return (prev + curr) / 2.0
        return float(curr)