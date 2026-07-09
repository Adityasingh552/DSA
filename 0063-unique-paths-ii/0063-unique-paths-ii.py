class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. Get dimensions first using the correct variable name
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 2. Base case: If start or end is blocked, no paths are possible
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
            
        # 3. Initialize grid with 0s and set the starting point to 1
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1

        # 4. Traverse the grid
        for i in range(m):
            for j in range(n):
                # Intercept obstacles first using single '=' to assign 0
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                    continue

                # Skip the start cell since it's already initialized to 1
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]