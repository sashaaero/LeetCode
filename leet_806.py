# https://leetcode.com/problems/number-of-lines-to-write-string/
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Number of Lines To Write String.

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        get_width = lambda sym: widths[ord(sym) - ord('a')]
        max_width = 100
        counter = 0
        for char in S:
            width = get_width(char)
            left = max_width - (counter % max_width)
            if width > left:
                counter += left
            counter += width

        a = counter // max_width
        b = counter % max_width
        if b != 0:
            a += 1
        return [a, b]

s = Solution()
widths = [5,7,4,7,6,7,9,5,8,8,5,10,9,10,2,5,7,9,3,8,8,8,10,2,2,9]
S = "lgrnv"
# print(s.numberOfLines(widths, S))
get_width = lambda sym: widths[ord(sym) - ord('a')]
counter = 0
for char in S:
    width = get_width(char)
    counter += width
    print(char, width, counter)

lines, width = 1, 0
for c in S:
    w = widths[ord(c) - ord('a')]
    width += w
    if width > 100:
        lines += 1
        width = w

    print(lines, width)
