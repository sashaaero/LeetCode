class Solution {
public:

    bool check(int x, int y, const vector<vector<int>>& grid) {
        vector<int> vis(10, false);
        int row = 0, col = 0;

        for (int i = x; i < x + 3; i++) {
            int tmp = 0;
            for (int j = y; j < y + 3; j++) {
                if (grid[i][j] >= 10 || vis[grid[i][j]])
                    return false;
                tmp += grid[i][j];
                vis[grid[i][j]] = true;
            }
            if (tmp != 15)
                return false;
        }

        for (int j = y; j < y + 3; j++) {
            int tmp = 0;
            for (int i = x; i < x + 3; i++)
                tmp += grid[i][j];
            if (tmp != 15)
                return false;
        }

        if (grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2] != 15)
            return false;
        if (grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y] != 15)
            return false;

        return true;
    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        for (int i = 0; i <= n - 3; i++)
            for (int j = 0; j <= m - 3; j++)
                if (check(i, j, grid))
                    ans++;
        return ans;
    }
};
