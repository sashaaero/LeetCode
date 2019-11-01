# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime: 52 ms, faster than 93.11% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        from heapq import merge
        nums = list(merge(nums1, nums2))
        if len(nums) % 2 == 0:
            i = len(nums) // 2
            return (nums[i] + nums[i-1]) / 2
        else:
            i = len(nums) // 2
            return nums[i]

if __name__ == '__main__':
    s = Solution()
    # s.findMedianSortedArrays([1,3,5,7], [2,4,8,9,10])
    assert s.findMedianSortedArrays([1,3], [2]) == 2.0
    assert s.findMedianSortedArrays([1,2], [3,4]) == 2.5