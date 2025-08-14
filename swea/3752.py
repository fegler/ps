T = int(input())

for t in range(1, T+1):
    N = int(input())
    vals = list(map(int, input().split()))
    dp = [0 for _ in range(sum(vals)+1)]
    dp[0] = 1 ## 다 틀림 
    for v in vals:
        for total in range(sum(vals), -1, -1):
            if dp[total]:
                dp[total+v] = 1
    print(f'#{t} {sum(dp)}')