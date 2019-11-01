# https://leetcode.com/problems/keys-and-rooms/
# Runtime: 40 ms, faster than 95.32% of Python3 online submissions for Keys and Rooms.

class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = set()

        def visit(room):
            visited.add(room)
            for r in rooms[room]:
                if r not in visited:
                    visit(r)

        visit(0)
        return len(visited) == N

s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(rooms))