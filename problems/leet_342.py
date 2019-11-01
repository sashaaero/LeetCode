# https://leetcode.com/problems/power-of-four/
# Runtime: 32 ms, faster than 95.27% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num == 0):
            return False
        while (num != 1):
            if (num % 4 != 0):
                return False
            num = num // 4
        return True
