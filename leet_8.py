# https://leetcode.com/problems/string-to-integer-atoi/
# Runtime: 40 ms, faster than 84.08% of Python3 online submissions for String to Integer (atoi).


class Solution:

    def process_value(self, value, negative):
        max_value = 2 ** 31 - 1
        min_value = -max_value - 1
        if negative:
            value = -value

        if value < min_value:
            return min_value
        elif value > max_value:
            return max_value
        return value

    def myAtoi(self, val):
        val = val.lstrip()
        res = 0
        negative = False
        i = 0
        if val.startswith('-'):
            negative = True
            i = 1
        elif val.startswith('+'):
            i = 1

        while i < len(val):
            char = val[i]
            if not char.isdigit():
                return self.process_value(res, negative)
            num = int(char)
            res *= 10
            res += num
            i += 1
        return self.process_value(res, negative)


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi("24") == 24
    assert s.myAtoi(" ") == 0
    assert s.myAtoi("   +21 lol") == 21
    assert s.myAtoi("   -2122 2 lol") == -2122
