"""
https://leetcode.com/problems/house-robber/
Runtime: 52 ms, faster than 7.54% of Python3 online submissions for House Robber.
Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.

"""


class Solution:
    def rob(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(array)
        if n == 0:
            return 0
        if n == 1:
            return array[0]
        dp = [[0,0] for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = array[0]
        dp[1][0] = array[0]
        dp[1][1] = array[1]
        for i in range(2,n):
            dp[i][0] = max(dp[i-2][0]+array[i-1],dp[i-2][1])
            dp[i][1] = max(dp[i-2][1]+array[i],dp[i-1][0]+array[i])
            #print(dp)
        return max(dp[n-1][0], dp[n-1][1])
        
