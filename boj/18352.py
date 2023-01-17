import sys 
from collections import deque 

input = sys.stdin.readline 

N,M,K,X = map(int, input().split())
visited = [0] * (N+1) 
adj_arr = [[] for _ in range(N+1)]
answer = []

for _ in range(M):
    s,t = map(int, input().split())
    adj_arr[s].append(t)

qu = deque()
qu.append((X, 0))
visited[X] = 1 
while qu:
    now, step = qu.popleft()
    if step == K:
        answer.append(now)
    for i in adj_arr[now]:
        if visited[i]: 
            continue 
        visited[i] = 1 
        qu.append((i, step+1))

if len(answer)==0:
    print("-1")
else:
    answer.sort()
    for i in answer:
        print(i)