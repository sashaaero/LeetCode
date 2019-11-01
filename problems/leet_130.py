"""
https://leetcode.com/problems/surrounded-regions/
Runtime: 168 ms, faster than 42.65% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.7 MB, less than 13.33% of Python3 online submissions for Surrounded Regions
"""


class Solution(object):
    def isValid(self,a,b,n,m):
        #print(a,b,n,m)
        if 0<=a and a<n and 0<=b and b<m:
            return True
        return False
            
    def bfs(self,sX,sY,n,m,board,visited):
        #print(sX,sY)
        visited[sX][sY] = True
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            if self.isValid(sX+dx[i],sY+dy[i],n,m) and board[sX+dx[i]][sY+dy[i]] == 'O' and visited[sX+dx[i]][sY+dy[i]] == False:
                self.bfs(sX+dx[i],sY+dy[i],n,m,board,visited)
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """ 
        if board == []:
            return []
        n = len(board)
        m = len(board[0])
        impossible = [[False]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1)  or (j==0 or j ==m-1):
                    if visited[i][j] == False and board[i][j] == 'O':
                        self.bfs(i,j,n,m,board,visited)
        for i in range(0,n):
            for j in range(0,m):
                if visited[i][j] == True:
                    continue
                else:
                    board[i][j] = 'X'
        
