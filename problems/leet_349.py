# https://leetcode.com/problems/intersection-of-two-arrays/
# Runtime: 44 ms, faster than 99.37% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))