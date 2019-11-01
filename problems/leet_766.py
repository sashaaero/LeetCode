# https://leetcode.com/problems/toeplitz-matrix/
# Runtime: 52 ms, faster than 91.93% of Python3 online submissions for Toeplitz Matrix.


matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

# matrix = [[83],[64],[57]]

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        if n == m == 1:
            return True

        # First we go from lower left to upper left
        i = n - 2
        j = 0
        while i > 0:
            x = i
            y = j
            curr = matrix[x][y]
            x += 1
            y += 1
            while x < n and y < m:
                if matrix[x][y] != curr:
                    return False
                x += 1
                y += 1
            i -= 1
            j = 0

        # from upper left to upper right
        i = 0
        j = 0
        while j < m - 1:
            x = i
            y = j
            curr = matrix[x][y]
            x += 1
            y += 1
            while x < n and y < m:
                if matrix[x][y] != curr:
                    return False
                x += 1
                y += 1
            i = 0
            j += 1

        return True

s = Solution()
print(s.isToeplitzMatrix(matrix))