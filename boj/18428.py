import sys 
from itertools import combinations

input = sys.stdin.readline 

N = int(input().rstrip())

board = [] 
teacher = [] 
empty_pos = []
for i in range(N):
    row = input().split()
    board.append(row)
    for j in range(N):
        if row[j] == 'T':
            teacher.append((i, j))
        elif row[j] == 'X':
            empty_pos.append((i,j))

def check_(board, teacher):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ret = True 
    for i in range(4):
        for x,y in teacher:
            now_x, now_y = x, y
            while True:
                now_x, now_y = now_x+dx[i], now_y+dy[i]
                if now_x<0 or now_x>=N or now_y<0 or now_y>=N or board[now_x][now_y] == 'O':
                    break 
                if board[now_x][now_y] == 'S':
                    return False 
    return ret 
                

answer = False
for pos in combinations(empty_pos, 3):
    for x,y in pos:
        board[x][y]='O'
    if check_(board, teacher):
        answer=True 
        break 
    for x,y in pos:
        board[x][y]='X'
if answer:
    print("YES")
else:
    print("NO")
        
