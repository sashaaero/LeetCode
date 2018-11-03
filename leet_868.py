# https://leetcode.com/problems/binary-gap/
# Runtime: 40 ms, faster than 90.86% of Python3 online submissions for Binary Gap.

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N.bit_length()
        result = 0
        prev_bit = -1
        mask = 1
        for i in range(n):
            bit = (N & mask) == mask
            if bit:
                if prev_bit == -1:
                    prev_bit = i
                else:
                    curr_bit = i
                    if (curr_bit - prev_bit) > result:
                        result = curr_bit - prev_bit
                    prev_bit = curr_bit
            mask <<= 1
        return result



s = Solution()
print(s.binaryGap(8))