# https://leetcode.com/problems/queue-reconstruction-by-height/


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return people
        people = sorted(people, key=lambda people: [-people[0], people[1]])
        result = []
        for h, i in people:
            result.insert(i, [h, i])
        return result

s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))