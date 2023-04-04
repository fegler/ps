import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
edge = {i: [] for i in range(1, N + 1)}
max_c = -1
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))
    edge[b].append((a, c))
    max_c = max(max_c, c)
x, y = map(int, input().split())
answer = -1


def bfs(num):
    global x, y, edge, N
    from collections import deque

    check = [0 for _ in range(N + 1)]
    qu = deque([])
    qu.append(x)
    check[x] = 1
    while qu:
        now = qu.popleft()
        if now == y:
            return 1
        for next, next_val in edge[now]:
            if next_val < num or check[next]:
                continue
            check[next] = 1
            qu.append(next)
    return 0


left = 1
right = max_c
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid 
        left = mid + 1
    else:
        right = mid - 1
print(answer)
