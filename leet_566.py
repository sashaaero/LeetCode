# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        if n * m != r * c:
            return nums

        result = [[nums[(j * c + i) // m][(j * c + i) % m] for i in range(c)] for j in range(r)]
        return result



s = Solution()
nums = [[1,2],[3,4]]

print(s.matrixReshape(nums, 1, 4))
