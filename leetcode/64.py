class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # for i in range(1, m):
        #     grid[i][0] += grid[i-1][0]
        # for i in range(1, n):
        #     grid[0][i] += grid[0][i-1]
        # for i in range(1, m):
        #     for j in range(1,n):
        #         grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # return grid[m-1][n-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j!=n-1:
                    grid[i][j] += grid[i][j+1]
                elif i!=m-1 and j==n-1:
                    grid[i][j] += grid[i+1][j]
                elif i!=m-1 and j!=n-1:
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]