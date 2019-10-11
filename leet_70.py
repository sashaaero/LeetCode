class Solution:
    def climbStairs(self, n: int, c=0) -> int:
        if n == 2:
	        return 2
        if n == 1:
            return 1
        if n == 0:
            return 0
        a = 0
        b = 1
        c = 0
        for i in range(n - 2):
	        a, b = b, a + b
	        c += b
        return(c + 2)