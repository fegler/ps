import sys 

N, M = map(int, input().split())
vals = list(map(int, sys.stdin.readline().split()))

def calc_tree(num):
    ret = 0
    for v in vals:
        if v > num:
            ret += (v-num)
    return ret 

l_val, r_val = 0, max(vals)
ret = 0 
while l_val <= r_val:
    mid_val = (l_val + r_val)//2
    get_val = calc_tree(mid_val)
    if get_val >= M:
        ret = mid_val
        l_val = mid_val + 1 
    else:
        r_val = mid_val - 1 
print(ret)