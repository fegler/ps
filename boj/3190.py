import re
import sys 
from collections import deque
input = sys.stdin.readline  
snake = deque()

N = int(input().rstrip())
K = int(input().rstrip())
board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int, input().split())
    board[x][y] = 1 
L = int(input().rstrip())
ch_info = []
for _ in range(L):
    num, direc = input().split()
    ch_info.append((int(num), direc))
ch_info.sort()
move_d = [(-1,0), (0,1), (1,0), (0,-1)]

def change_direc(now, command):
    if command == 'L':
        if now == 0: 
            return 3
        else:
            return now-1
    elif command == 'D':
        if now == 3:
            return 0
        else: 
            return now + 1

## main simulation 
board[1][1] = 2 
x, y = 1, 1
snake.appendleft((x, y))
direc = 1
answer = 0
for i in range(1, N*N):
    ## next position 
    x, y = x+move_d[direc][0], y+move_d[direc][1]
    
    if x<1 or y<1 or x>N or y>N or board[x][y]==2: 
        ## game over
        answer = i 
        break 
    
    snake.appendleft((x,y))
    if board[x][y]!=1:
        pop_info = snake.pop()
        board[pop_info[0]][pop_info[1]] = 0 
    board[x][y]=2 

    ## change direction 
    if len(ch_info)!=0 and i == ch_info[0][0]:
        direc = change_direc(direc, ch_info[0][1])
        ch_info.pop(0)
print(answer)