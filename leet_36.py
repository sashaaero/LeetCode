# https://leetcode.com/problems/valid-sudoku/
# Runtime: 40 ms, faster than 98.65% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board):
        # validate rows
        for row in board:
            values = set()
            for cell in row:
                if cell != '.':
                    if cell in values:
                        return False
                    values.add(cell)

        # validate cols
        i, j = 0, 0
        while i < 9:
            values = set()
            j = 0
            while j < 9:
                cell = board[j][i]
                if cell != '.':
                    if cell in values:
                        return False
                    values.add(cell)
                j += 1
            i += 1
        # validate districts
        for dx in range(3):
            cur_dx = 3 * dx
            for dy in range(3):
                values = set()
                cur_dy = 3 * dy
                for i in range(cur_dx, cur_dx + 3):
                    for j in range(cur_dy, cur_dy + 3):
                        cell = board[i][j]
                        if cell != '.':
                            if cell in values:
                                return False
                            values.add(cell)

        return True


if __name__ == '__main__':
    s = Solution()
    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],        
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    assert s.isValidSudoku(board) == False