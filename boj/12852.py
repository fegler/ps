N = int(input())

dp = [0] * (N+1)
track = [-1] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 
    track[i] = i-1

    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2] + 1 
        track[i] = i//2 
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1 
        track[i] = i//3 

print(dp[N])

now = N 
while now != 1:
    print(now, end=' ')
    now = track[now]
print('1')