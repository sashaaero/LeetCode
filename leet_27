# https://leetcode.com/problems/remove-element/submissions/
# Runtime: 40 ms, faster than 69.97% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1 
        while i >= 0:
            if nums[i] == val:
                del nums[i]
            i -= 1
            
        return len(nums)
