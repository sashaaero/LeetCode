#https://leetcode.com/problems/assign-cookies/
#Runtime: 144 ms, faster than 89.29% of Python online submissions for Assign Cookies. Memory Usage: 13 MB, less than 66.67% of Python online submissions for Assign Cookies.
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        gi=0
        si=0
        g.sort(reverse=True)
        s.sort(reverse=True)
        while gi<len(g) and si<len(s):
            if g[gi]>s[si]:
                gi+=1
            else:
                gi+=1
                si+=1

        return si
