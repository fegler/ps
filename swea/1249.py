from collections import defaultdict 
import heapq

direction = [(-1,0),(1,0),(0,1),(0,-1)]

def dfs(now_y, now_x, now_cost):
    global grid, N, memo, direction
    if now_cost >= memo[now_y][now_x]:
        return 
    memo[now_y][now_x] = now_cost
    for dy, dx in direction:
        next_y, next_x = now_y+dy, now_x+dx 
        if next_y<0 or next_y>=N or next_x<0 or next_x>=N:
            continue 
        dfs(next_y, next_x, now_cost+grid[next_y][next_x])

T = int(input())
direction = [(-1,0), (1,0), (0,-1), (0,1)]
for i in range(1, T+1):
    N = int(input())
    grid = []
    memo = [[987654321] * N for _ in range(N)]
    for _ in range(N):
        line = input().strip() 
        now = []
        for v in line:
            now.append(int(v))
        grid.append(now)

    dfs(0,0, grid[0][0])

    print(f'#{i} {memo[N-1][N-1]}')