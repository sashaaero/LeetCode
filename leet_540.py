# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Runtime: 36 ms, faster than 91.98% of Python3 online submissions for Single Element in a Sorted Array.

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if m - 1 < l or m + 1 > r:
                break
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m
        return nums[l]

s = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(nums))