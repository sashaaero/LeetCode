// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
// Runtime: 36 ms, faster than 94.80% of C++ online submissions for Longest Increasing Path in a Matrix.

class Solution {
public:
    int **mask;
    size_t current_longest_path, current_path_length, colsize, rowsize;
    void init(vector<vector<int>>& matrix)
    {
        colsize = matrix.size();
        rowsize = matrix[0].size();
        mask = new int* [matrix.size()];
        for (int i = 0; i < matrix.size(); ++i)
        {
            mask[i] = new int[matrix[0].size()];
        }
        zero_mask();
    }
    void zero_mask()
    {
        for (auto i = 0; i < colsize; ++i)
        {
            for (auto j = 0; j < rowsize; ++j)
            {
                mask[i][j] = 0;
            }   
        }
    }
    void do_search(vector<vector<int>>& matrix, int elem, size_t i, size_t j)
    {
        mask[i][j] = 1;
        bool final_elem = true;
        if (i != 0 && elem < matrix[i-1][j] && !(mask[i-1][j]))
        {
            // up
            final_elem = false;
            current_path_length++;
            if (current_path_length > current_longest_path)
            {
                current_longest_path = current_path_length;
            }
            ]
            do_search(matrix, matrix[i-1][j], i-1 ,j);
        }
        if (i != colsize-1 && elem < matrix[i+1][j] && !(mask[i+1][j]))
        {
            // down
            final_elem = false;
            current_path_length++;
            if (current_path_length > current_longest_path)
            {
                current_longest_path = current_path_length;
            }
            do_search(matrix, matrix[i+1][j], i+1 ,j);
        }
        if (j != 0 && elem < matrix[i][j-1] && !(mask[i][j-1]))
        {
            // left
            final_elem = false;
            current_path_length++;
            if (current_path_length > current_longest_path)
            {
                current_longest_path = current_path_length;
            }
            do_search(matrix, matrix[i][j-1], i ,j-1);
        }
        if (j != rowsize-1 && elem < matrix[i][j+1] && !(mask[i][j+1]))
        {
            // right
            final_elem = false;
            current_path_length++;
            if (current_path_length > current_longest_path)
            {
                current_longest_path = current_path_length;
            }
            do_search(matrix, matrix[i][j+1], i ,j+1);
        }
        if(final_elem)
        { 
            mask[i][j] = 0;
        }
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        init(matrix); 
        current_longest_path = 1;       
        for (auto i = 0; i != colsize; ++i)
        {
            for (auto j = 0; j != rowsize; ++j)
            {          
                current_path_length = 1;      
                do_search(matrix, matrix[i][j], i ,j);
            } 
        }
        return current_longest_path;
    }
};