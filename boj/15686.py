import sys 
from itertools import combinations 
from collections import deque

input = sys.stdin.readline 

N, M = map(int, input().split())
board = [] 
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dist = {}
home_pos = {}

def set_check(c):
    for i in range(N):
        for j in range(N):
            c[i][j]=0
    return c 

def bfs(c_idx, y, x):
    global dist 
    check = [[0 for _ in range(N)] for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    qu = deque()
    check[y][x]=1 
    qu.append((y,x,0))
    while qu:
        now_y, now_x, step = qu.popleft()
        if board[now_y][now_x] == 1: 
            if not (now_y, now_x) in dist.keys():
                dist[(now_y, now_x)] = [(step, c_idx)]
            else:
                dist[(now_y, now_x)].append((step, c_idx))
        for i in range(4):
            next_y, next_x = now_y+dy[i], now_x+dx[i]
            if next_y<0 or next_y>=N or next_x<0 or next_x>=N or check[next_y][next_x]: continue  
            check[next_y][next_x] = 1 
            qu.append((next_y, next_x, step+1))

num = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            bfs(num, i, j)
            num += 1
        if board[i][j] == 1: 
            home_pos[(i,j)] = None

chicken = [i for i in range(1, num)]
for i in home_pos.keys():
    dist[i].sort()

chicken_comb = list(combinations(chicken, (num-1)-M))
answer = 987654321
if len(chicken_comb)==1 and len(chicken_comb[0])==0:
    answer = [dist[i][0][0] for i in home_pos.keys()]
    answer = sum(answer)
    print(answer)
else:
    for comb in chicken_comb:
        tmp_answer = 0
        no_select_home_exist = False
        for i in home_pos.keys(): 
            for j in range(len(dist[i])):
                now = dist[i][j]
                if now[1] in comb:
                    if j==len(dist[i])-1:
                        no_select_home_exist = True  
                    continue 
                tmp_answer += now[0]
                break 
        if no_select_home_exist:
            continue 
        answer = min(answer, tmp_answer)
    print(answer)