from collections import deque, defaultdict 

# T = int(input())
T = 10 
up_direc = (-1, 0)
search_direc = [(0,-1), (0,1)]
    

def dfs(now_y, now_x):
    global grid, up_direc, search_direc, visited
    if now_y == 0:
        ## end point 
        return now_x 
    
    move_flag = False
    for dy, dx in search_direc:
        next_y, next_x = now_y+dy, now_x+dx 
        if next_y<0 or next_y>=100 or next_x<0 or next_x>=100:
            continue
        if (next_y, next_x) in visited:
            continue 
        if grid[next_y][next_x] == 1:
            visited.add((next_y, next_x))
            move_flag = True 
            return dfs(next_y, next_x)
             
    
    if not move_flag:
        next_y, next_x = now_y+up_direc[0], now_x+up_direc[1]
        visited.add((next_y, next_x))
        return dfs(next_y, next_x)

for idx in range(1, T+1):
    t = int(input())
    grid = [] 
    for _ in range(100):
        line = list(map(int, input().split()))
        grid.append(line)
    start_x = -1 
    for i in range(100):
        if grid[99][i] == 2:
            start_x = i 
            break 
    visited = set()

    print(f'#{idx} {dfs(99, start_x)}')
