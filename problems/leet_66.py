# https://leetcode.com/problems/plus-one/
# Runtime: 36 ms, faster than 99.69% of Python3 online submissions for Plus One.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            digits[i] = (digits[i] + 1) if digits[i] < 9 else 0
            if digits[i] != 0:
                return digits
            i -= 1
        if digits[0] == 0:
            return [1] + digits
        return digits
