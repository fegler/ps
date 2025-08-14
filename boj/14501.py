N = int(input())

vals = []
vals.append((0,0))
for i in range(N):
    t, p = map(int, input().split())
    vals.append((t, p))

dp = [0 for _ in range(N+2)]

for i in range(1, N+1):
    now_t, now_p = vals[i]
    dp[i] = max(dp[i], dp[i-1])

    if i + now_t <= N+1:
        dp[i+now_t] = max(dp[i+now_t], dp[i]+now_p)

# print(dp)
max_val = 0
for v in dp:
    max_val = max(max_val, v)
print(max_val)