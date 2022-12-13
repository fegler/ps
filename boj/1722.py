import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
arr = list(map(int, input().split()))
command = arr[0]
perm = [1]*(N+1)
for i in range(1, N+1):
    perm[i] *= (perm[i-1]*i)
    
if command == 1: 
    perm_answer = ''
    k = arr[1]
    val = [i for i in range(1, N+1)]
    answer = '' 
    for i in range(N-1, -1, -1):
        if k > perm[i]:
            a = k//perm[i]
            b = k%perm[i]
            if b==0: a-=1 
            now = val[a]
            k=b
        else: 
            if k==0: now=val[-1]
            else: now = val[0]
        answer += (str(now)+ ' ')
        val.remove(now)
    print(answer)
else:
    arr = arr[1:]
    val = [i for i in range(1, N+1)]
    answer = 0
    for now in arr: 
        if val[0] != now:
            answer += (val.index(now) * perm[len(val)-1])
        val.remove(now)
    print(answer+1) 
