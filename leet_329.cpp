// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
// Runtime: 36 ms, faster than 94.80% of C++ online submissions for Longest Increasing Path in a Matrix.

class Solution {
public:
    int** mask;
    size_t colsize, rowsize;
    void init(vector<vector<int>>& matrix)
    {
        colsize = matrix.size();
        rowsize = matrix[0].size();
        mask = new int* [matrix.size()];
        for (int i = 0; i < matrix.size(); ++i)
        {
            mask[i] = new int[matrix[0].size()];
        }
        for (auto i = 0; i < colsize; ++i)
        {
            for (auto j = 0; j < rowsize; ++j)
            {
                mask[i][j] = 0;
            }
        }
    }

    short do_search(vector<vector<int>>& matrix, size_t i, size_t j)
    {
        if (mask[i][j]) return mask[i][j];
        size_t current_path = 1, new_path;
        int elem = matrix[i][j];
        if (i != 0 && elem < matrix[i - 1][j])
        {
            // up
            current_path += do_search(matrix, i - 1, j);
        }
        if (j != 0 && elem < matrix[i][j - 1])
        {
            // left
            new_path = do_search(matrix, i, j - 1);
            if (current_path < new_path + 1)
                current_path = new_path + 1;
        }
        if (j != rowsize - 1 && elem < matrix[i][j + 1])
        {
            // right
            new_path = do_search(matrix, i, j + 1);
            if (current_path < new_path + 1)
                current_path = new_path + 1;
        }
        if (i != colsize - 1 && elem < matrix[i + 1][j])
        {
            // down
            new_path = do_search(matrix, i + 1, j);
            if (current_path < new_path + 1)
                current_path = new_path + 1;
        }
        mask[i][j] = current_path;
        return current_path;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.size() == 0) return 0;
        init(matrix);
        size_t current_longest_path = 1, last_path;
        for (auto i = 0; i != colsize; ++i)
        {
            for (auto j = 0; j != rowsize; ++j)
            {
                last_path = do_search(matrix, i, j);
                if (last_path > current_longest_path)
                    current_longest_path = last_path;
            }
        }
        return current_longest_path;
    }
};