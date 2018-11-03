# https://leetcode.com/problems/baseball-game/
# Runtime: 36 ms, faster than 98.79% of Python3 online submissions for Baseball Game.


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)




s = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(s.calPoints(ops))
