# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 52 ms	python3 Your runtime beats 91.90 % of python3 submissions.

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        return list((counter1 & counter2).elements())
