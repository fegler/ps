N = int(input())

## i-day부터 마지막날까지 상담했을 때, 최대 수익 
dp = [0 for _ in range(N+2)]
vals = [(0,0),] 
for _ in range(N):
    t, p = map(int, input().split())
    vals.append((t, p))

for i in range(N, 0, -1):
    now_t, now_p = vals[i]
    if i + now_t <= N+1:
        ## 사용 가능 
        dp[i] = max(dp[i+1], dp[i+now_t]+now_p)
    else:
        dp[i] = dp[i+1]
print(dp[1])