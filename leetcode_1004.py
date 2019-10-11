"""
https://leetcode.com/problems/max-consecutive-ones-iii/
Runtime: 776 ms, faster than 22.36% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.3 MB, less than 16.67% of Python3 online submissions for Max Consecutive Ones III.
"""

class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        i,j,maxCount,maxLength = 0,0,0,0
        while(j<len(A)):
            if A[j] == 1:
                maxCount+=1
            if j-i+1-maxCount > k:
                if A[i] == 1:
                    maxCount-=1
                i+=1
            maxLength = max(maxLength,j-i+1)
            j+=1
        return maxLength
        
