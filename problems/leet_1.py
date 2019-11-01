# https://leetcode.com/problems/two-sum
# Runtime: 32 ms, faster than 90.53% of Python online submissions for Two Sum.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1]
