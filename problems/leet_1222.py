class Solution(object):
    def queensAttacktheKing(self, queens, king):
        queens_dict = {(x,y): 1 for x,y in queens}
        directions = [[-1,0], [1,0], [0,-1], [0,1],
                    [-1,-1], [1,1], [-1,1], [1,-1] ]
        queens = []
        for xd,yd in directions:
            x,y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += xd
                y += yd
                if (x,y) in queens_dict:
                    queens.append([x, y])
                    break
        return queens

