import sys

input = sys.stdin.readline

N = int(input().strip())

num = []
for _ in range(N):
    now = list(map(int, input().split()))
    num.append(now)

for i in range(N - 2, -1, -1):
    for j in range(i + 1):
        num[i][j] += max(num[i + 1][j], num[i + 1][j + 1])
print(num[0][0])
