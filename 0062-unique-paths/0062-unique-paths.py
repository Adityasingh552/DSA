class Solution:
    def uniquePaths(self, m: int, n: int):

        grid = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]