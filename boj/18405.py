import sys 
from collections import deque 

input = sys.stdin.readline

N,K = map(int, input().split())
board = [] 
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
S, X, Y = map(int, input().split()) 
visited = [[0 for _ in range(N)] for _ in range(N)]

answer = [1005, 50000] ## first meet virus, step
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
qu = deque()
qu.append((X-1,Y-1,0))
visited[X-1][Y-1] = 1
while qu: 
    now_x, now_y, step = qu.popleft()
    if board[now_x][now_y] > 0:
        if answer[1] > step:
            answer[0] = board[now_x][now_y]
            answer[1] = step 
        elif answer[1] == step:
            answer[0] = min(answer[0], board[now_x][now_y])
        else:
            continue 
    for i in range(4):
        next_x, next_y = now_x+dx[i], now_y+dy[i]
        if next_x<0 or next_x>=N or next_y<0 or next_y>=N: continue 
        if visited[next_x][next_y]:
            continue 
        qu.append((next_x, next_y, step+1))
        visited[next_x][next_y] = 1
if answer[1] > S:
    print('0')
else:
    print(answer[0])

