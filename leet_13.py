# https://leetcode.com/problems/roman-to-integer/
# Runtime: 52 ms, faster than 96.13% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = None
        for sym in s:
            res += values[sym]
            if sym in ('D', 'M') and prev == 'C':
                res -= 200
            elif sym in ('L', 'C') and prev == 'X':
                res -= 20
            elif sym in ('V', 'X') and prev == 'I':
                res -= 2
            prev = sym
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt('III') == 3
    assert s.romanToInt('IV') == 4
    assert s.romanToInt('IX') == 9
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994
