import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

indegree = [0 for _ in range(N + 1)]
edge = {i: [] for i in range(1, N + 1)}
answer = {i: [0 for _ in range(N)] for i in range(1, N + 1)}
qu = deque([])

for _ in range(M):
    x, y, k = map(int, input().split())
    indegree[x] += 1
    edge[x].append((y, k))

for i in range(1, N):
    if indegree[i] == 0:
        answer[i][i] = 1


def update_ans(l1, l2, num):
    return [l1[i] + l2[i] * num for i in range(len(l1))]


def dfs(n):
    if sum(answer[n]) != 0:
        return answer[n]
    for next, next_val in edge[n]:
        answer[n] = update_ans(answer[n], dfs(next), next_val)
    return answer[n]


final_ans = dfs(N)
for i in range(N):
    if final_ans[i] != 0:
        print(i, final_ans[i])
