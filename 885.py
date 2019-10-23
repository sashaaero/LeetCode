class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = [[r0, c0]]
        step = 1
        while len(res) < R*C:
            for i in range(step):
                r0 = r0
                c0 = c0 + 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
            for i in range(step):
                r0 = r0 + 1
                c0 = c0
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
            step += 1
            for i in range(step):
                r0 = r0
                c0 = c0 - 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
            for i in range(step):
                r0 = r0 - 1
                c0 = c0
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
            step += 1
        return res
