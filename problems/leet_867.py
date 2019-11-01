# https://leetcode.com/problems/transpose-matrix/
# Runtime: 60 ms, faster than 85.24% of Python3 online submissions for Transpose Matrix.


def transpose(A):
    mat = [[] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for g in range(len(A)):
            mat[i].append(A[g][i])
    return mat


A1 = [[1,2,3],[4,5,6],[7,8,9]]
A2 = [[1,2,3],[4,5,6]]

print(transpose(A2))