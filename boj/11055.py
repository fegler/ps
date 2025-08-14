N = int(input())
vals = list(map(int, input().split()))
dp = [v for v in vals]

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if vals[i] > vals[j]:
            dp[i] = max(dp[i], dp[j]+vals[i])
max_val = -1
for i in range(N):
    max_val = max(max_val, dp[i])
print(max_val)