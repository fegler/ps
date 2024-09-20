class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(l))] for l in triangle]
        def recur(row, col):
            if row == len(triangle)-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = triangle[row][col] + min(
                recur(row+1, col), recur(row+1, col+1)
            )
            return dp[row][col]
        dp[0][0] = recur(0,0)
        return dp[0][0]