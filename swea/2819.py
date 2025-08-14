from collections import deque, defaultdict 

T = int(input())
direction = [(-1,0), (1,0), (0,-1), (0,1)]

for idx in range(1, T+1):
    grid = []
    for _ in range(4):
        line = list(map(int, input().split()))
        grid.append(line)
    total_seq = set()
    qu = deque([])
    for i in range(4):
        for j in range(4):
            qu.append((str(grid[i][j]), (i, j)))
    while qu:
        now_val, (now_y, now_x) = qu.popleft() 
        if len(now_val) == 7:
            total_seq.add(now_val)
            continue 
        for dy, dx in direction:
            next_y, next_x = now_y+dy, now_x+dx 
            if next_y<0 or next_y>=4 or next_x<0 or next_x>=4:
                continue 
            next_val = now_val + str(grid[next_y][next_x])
            qu.append((next_val, (next_y, next_x)))
    print(f'#{idx} {len(total_seq)}')
