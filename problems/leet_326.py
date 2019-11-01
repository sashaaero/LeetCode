# https://leetcode.com/problems/power-of-three/submissions/
# Runtime: 84 ms, faster than 81.89% of Python3 online submissions for Power of Three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n != 0 and n > 0:
            if 1162261467 % n == 0:
                return True
        return False