import sys 
from heapq import heappush, heappop 

input = sys.stdin.readline 

N = int(input().rstrip())

val = []
for _ in range(N):
    tmp = int(input().rstrip())
    heappush(val, tmp)

answer = 0 
while val: 
    val1 = heappop(val)
    if not val:
        break
    else:
        val2 = heappop(val)
    
    answer += (val1+val2)
    heappush(val, val1+val2)
print(answer)
    