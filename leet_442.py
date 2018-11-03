# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Runtime: 152 ms, faster than 94.46% of Python3 online submissions for Find All Duplicates in an Array.

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cont = set()
        result = []
        for num in nums:
            if num not in cont:
                cont.add(num)
            else:
                result.append(num)
        return result

s = Solution()
nums = [4,3,2,7,8,2,3,1]
ans = [2,3]
assert ans == s.findDuplicates(nums)