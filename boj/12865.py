import sys 
N, K = map(int, input().split())
obj = []
for _ in range(N):
    n, w = map(int, sys.stdin.readline().split())
    obj.append((n, w))
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        if j >= obj[i-1][0]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-obj[i-1][0]]+obj[i-1][1])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
# print(dp)
print(dp[N][K])