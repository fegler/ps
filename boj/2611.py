import sys 
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
edge = {i: [] for i in range(1, N+1)}
dp = [-1 for _ in range(N+1)]
dp_nodes = [[] for _ in range(N+1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    edge[p].append([q, r])

def dfs(now):
    global edge, dp, dp_nodes 

    if dp[now] != -1:
        return dp[now], dp_nodes[now]
    
    ret = 0
    dp[now] = 0 
    for next, next_val in edge[now]:
        val, nodes = dfs(next)
        if ret < val+next_val:
            ret = val+next_val
            ret_nodes = [next] + nodes
    dp[now] += ret 
    dp_nodes[now] += ret_nodes   
    return dp[now], dp_nodes[now]

val, nodes = dfs(1)
print(val)
nodes = [1] + nodes
for i in nodes:
    print(i, end=' ')