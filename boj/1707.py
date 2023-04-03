import sys
from collections import deque

input = sys.stdin.readline

K = int(input().strip())


def next_color(now):
    return (now + 1) % 2


def solve():
    V, E = map(int, input().split())
    v_dict = {}
    check = [-1 for _ in range(V + 1)]
    qu = deque([])
    for i in range(V):
        v_dict[i + 1] = []
    for _ in range(E):
        v1, v2 = map(int, input().split())
        v_dict[v1].append(v2)
        v_dict[v2].append(v1)
    for i in range(1, V + 1):
        if check[i] != -1:
            continue
        check[i] = next_color(check[i])
        qu.append((i, check[i]))
        while qu:
            now, now_color = qu.popleft()
            for next in v_dict[now]:
                if check[next] == -1:
                    check[next] = next_color(now_color)
                    qu.append((next, check[next]))
                elif check[next] == now_color:
                    return 0
    return 1


for _ in range(K):
    if solve():
        print("YES")
    else:
        print("NO")
