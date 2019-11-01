# https://leetcode.com/problems/reverse-integer
# Runtime: 12 ms, faster than 96.32% of Python online submissions for Reverse Integer.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))

        reversed = int(s[::-1])

        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)

if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
