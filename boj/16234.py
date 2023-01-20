import sys 
from collections import deque 

input = sys.stdin.readline 

N,L,R = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

def move_people(board):
    num = 1
    global N
    united = [[0 for _ in range(N)] for _ in range(N)]
    is_move = False
    for i in range(N):
        for j in range(N):
            if united[i][j] == 0:
                united, sum_val, country_list = bfs(board, united, i, j, num)
                num += 1 
                u_num = len(country_list)
                val = sum_val // u_num
                if u_num == 1: continue 
                else:
                    for x,y in country_list: 
                        board[x][y] = val  
                    is_move = True 
    return board, is_move 

def bfs(board, united, x, y, num):
    qu = deque()
    global N, L, R
    country_list = []
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    qu.append((x,y))
    united[x][y] = num
    sum_val = 0 
    while qu:
        now_x, now_y = qu.popleft()
        country_list.append((now_x, now_y))
        sum_val += board[now_x][now_y]
        for i in range(4):
            next_x, next_y = now_x+dx[i], now_y+dy[i]
            if next_x<0 or next_x>=N or next_y<0 or next_y>=N: continue 
            if united[next_x][next_y] > 0: continue 
            val = abs(board[now_x][now_y] - board[next_x][next_y])
            if val >= L and val <= R:
                qu.append((next_x, next_y))
                united[next_x][next_y] = num 
    return united, sum_val, country_list

answer = 0 
while True:
    board, is_move = move_people(board)
    if not is_move:
        break
    else:
        answer += 1 
print(answer)
