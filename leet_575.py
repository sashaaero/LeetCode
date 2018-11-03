# https://leetcode.com/problems/distribute-candies/
# Runtime: 124 ms, faster than 95.30% of Python3 online submissions for Distribute Candies.

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) // 2)


s = Solution()
candies = [1,1,2,2,3,3]
print(s.distributeCandies(candies))
