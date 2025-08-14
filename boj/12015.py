N = int(input())
vals = list(map(int, input().split()))

tails = []
tails.append(vals[0])

def find_idx(val):
    global tails 
    left, right = 0, len(tails)
    while left < right: 
        mid = (left+right)//2 
        if tails[mid] < val:
            left = mid + 1 
        else:
            right = mid 
    return left 

for i in range(1, len(vals)):
    idx = find_idx(vals[i])
    if idx == len(tails):
        tails.append(vals[i])
    else:
        tails[idx] = min(tails[idx], vals[i])
print(len(tails))