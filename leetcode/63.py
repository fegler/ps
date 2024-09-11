class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0] = 1
        flag=False
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                flag=True 
            elif not flag:
                obstacleGrid[i][0] = 1
        flag=False
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
                flag=True
            elif not flag:
                obstacleGrid[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]