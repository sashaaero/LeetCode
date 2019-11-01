# https://leetcode.com/problems/island-perimeter/
# Runtime: 284 ms, faster than 83.20% of Python3 online submissions for Island Perimeter.

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                elem = grid[i][j]
                if elem != 0:
                    # check upper
                    if i == 0:
                        counter += 1
                    else:
                        counter += grid[i-1][j] == 0
                    # check right
                    if j == m - 1:
                        counter += 1
                    else:
                        counter += grid[i][j+1] == 0
                    # check lower
                    if i == n - 1:
                        counter += 1
                    else:
                        counter += grid[i+1][j] == 0
                    # check left
                    if j == 0:
                        counter += 1
                    else:
                        counter += grid[i][j-1] == 0
        return counter


grid = [
     [0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
s = Solution()
print(s.islandPerimeter(grid))