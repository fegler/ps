N = int(input())

vals = list(map(int, input().split()))
tail = []
tail.append(vals[0])

def find_idx(val):
    global vals 
    left, right = 0, len(tail)
    while left < right:
        mid = (left+right) // 2 
        if tail[mid] < val:
            left = mid+1 
        else:
            right = mid
    return left

for i in range(1, N):
    insert_idx = find_idx(vals[i])
    if insert_idx == len(tail):
        tail.append(vals[i])
    else:
        tail[insert_idx] = min(tail[insert_idx], vals[i])

print(len(tail))