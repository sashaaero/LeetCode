# https://leetcode.com/problems/fizz-buzz/
# Runtime: 52 ms, faster than 98.59% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))

        return result

s = Solution()
n = 15
print(s.fizzBuzz(n))