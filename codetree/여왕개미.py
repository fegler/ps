from collections import defaultdict
Q = int(input().strip())

house_info = defaultdict(int)
next_idx = -1

def _init(inputs):
    global house_info, next_idx
    n = int(inputs[1])
    next_idx = n+1
    x_list = map(int, inputs[2:])
    for idx, x in enumerate(x_list):
        house_info[idx+1] = x

def _build(inputs):
    global house_info, next_idx 
    p = int(inputs[1])
    house_info[next_idx] = p 
    next_idx += 1 

def _remove(inputs):
    global house_info
    q = int(inputs[1]) 
    del house_info[q]

def _find(inputs):
    global house_info, next_idx 
    r = int(inputs[1])

    ## no move 
    if r >= len(house_info.keys()):
        print('0')
        return 

    ## max id, pos 
    max_idx, max_pos = -1, -1
    for idx in range(next_idx,-1,-1):
        if idx in house_info:
            max_idx, max_pos = idx, house_info[idx]
            break 
    ## min id, pos 
    min_idx, min_pos = -1, -1 
    for idx in range(1, next_idx):
        if idx in house_info:
            min_idx, min_pos = idx, house_info[idx]
            break 

    def check_ok(dist):
        total_num = len(house_info.keys())
        processed, now_r = 0, r
        if now_r <= 0:
            return False 
        
        ## assign ant to first house
        now_r -= 1 
        now_pos = min_pos

        for idx, pos in house_info.items():

            if pos - now_pos > dist: ## assign new ant 
                now_r -= 1
                now_pos = pos

            if now_r < 0: ## no ant 
                return False  
            processed += 1 
            if total_num - processed <= now_r:
                return True
    
    left, right = 0, max_pos 
    answer = right 
    while left <= right:
        mid = (left + right) // 2 
        if check_ok(mid):
            answer = mid 
            right = mid - 1 
        else:
            left = mid + 1
    print(answer)

for _ in range(Q):
    inputs = input().split()
    if inputs[0] == '100':
        _init(inputs)
    elif inputs[0] == '200':
        _build(inputs)
    elif inputs[0] == '300':
        _remove(inputs)
    else:
        _find(inputs)