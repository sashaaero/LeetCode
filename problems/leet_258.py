# https://leetcode.com/problems/add-digits/
# Runtime: 0 ms, faster than 100.00% of C online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        if(num==0):
            return 0
        if(num%9==0):
            return 9
        return num%9
        

s = Solution()
number = 38
print(s.addDigits(number))
