class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            arr[i][0] = 1 
        for i in range(n):
            arr[0][i] = 1 
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[m-1][n-1]