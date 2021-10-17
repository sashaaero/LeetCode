# https://leetcode.com/problems/find-the-difference/
# Runtime: 36 ms, faster than 68.64% of Python3 online submissions for Find the Difference.


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpha = dict()
        for each_s in s:
            if each_s not in alpha:
                alpha[each_s] = 1
            else:
                alpha[each_s]+=1
        for each_t in t:
            if each_t in alpha:
                alpha[each_t] -=1
            else:
                alpha[each_t] = 1
        string=""
        for key,value in alpha.items():
            if(value==1 or value==-1):
                string+=key
        print(string)
        return string
        

s = Solution()
print(s.findTheDifference("abcd", "abcde"))


