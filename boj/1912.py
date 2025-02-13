import sys 
N = int(input())
vals = list(map(int, sys.stdin.readline().split()))

def recur(left, right):
    ## [left, right]
    if left == right:
        return vals[left]
    mid = (left+right) // 2
    left_val = recur(left, mid)
    right_val = recur(mid+1, right)
    contain_mid_val = cal_mid(left, mid, right)
    return max(max(left_val, right_val), contain_mid_val)

def cal_mid(left, mid, right):
    l_sum, r_sum = -1000000000, -100000000
    sum = 0 
    for i in range(mid, left-1, -1):
        sum += vals[i]
        l_sum = max(l_sum, sum)
    sum = 0 
    for i in range(mid+1, right+1):
        sum += vals[i]
        r_sum = max(r_sum, sum)
    return l_sum+r_sum

if N == 1:
    print(vals[0])
elif N == 2:
    sum_val = vals[0]+vals[1]
    print(max(sum_val, max(vals[0], vals[1])))
else:
    print(recur(0, N-1))