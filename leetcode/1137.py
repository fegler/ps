class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1 
        memo = [-1 for _ in range(n+1)]
        memo[0], memo[1], memo[2] = 0, 1, 1
        def recur(now):
            if memo[now] != -1:
                return memo[now]
            memo[now] = recur(now-3) + recur(now-2) + recur(now-1)
            return memo[now]
        return recur(n)
            