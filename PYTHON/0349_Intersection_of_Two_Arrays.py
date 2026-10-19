#05/08/2026
#Easy
#Intersection of Two Arrays
# LeetCode: Find the unique intersection of two integer arrays using sets.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))