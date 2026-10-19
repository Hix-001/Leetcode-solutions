# 23/08/2026
# Easy
# LeetCode 350: Intersection of Two Arrays II using a frequency map.

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            
        res = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                res.append(num)
                counts[num] -= 1
                
        return res