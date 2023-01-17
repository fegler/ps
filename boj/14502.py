import sys
from collections import deque
from itertools import combinations
import copy 

input = sys.stdin.readline 

N,M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = -1 

empty_pos = []
virus_pos = [] 
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 0:
            empty_pos.append((i,j))
        if row[j] == 2:
            virus_pos.append((i,j))
        board[i][j] = row[j]

for c in combinations(empty_pos, 3):
    for x,y in c:
        board[x][y] = 1
    qu = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    num = 3 
    for x,y in virus_pos:
        qu.append((x,y))
        visited[x][y] = 1 
    while qu:
        now_x, now_y = qu.popleft()
        if board[now_x][now_y] == 0:
            num += 1 
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if next_x<0 or next_x>=N or next_y<0 or next_y>=M or visited[next_x][next_y] or board[next_x][next_y]==1:
                continue 
            qu.append((next_x, next_y))
            visited[next_x][next_y] = 1
    
    answer = max(answer, len(empty_pos)-num)
    for x,y in c:
        board[x][y] = 0

print(answer)