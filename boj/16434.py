import sys 
import math
input = sys.stdin.readline

N, H_atk = map(int, input().split())
need_hp, max_hp = 0, 0 

for _ in range(N):
    t, a, h = map(int, input().split())
    if t == 1:
        ## monster 
        need_hp += ((math.ceil(float(h)/H_atk)-1) * a)
        max_hp = max(max_hp, need_hp+1)
    else: 
        ## potion 
        need_hp = max(0, need_hp - h)
        H_atk += a 
print(max_hp)