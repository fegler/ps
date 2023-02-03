import sys 
sys.setrecursionlimit(1000000)

input = sys.stdin.readline 

N, C = map(int, input().split())
home = [] 
start, end = 0, 0
for i in range(N):
    now = int(input().strip())
    home.append(now)
    if i==0:
        start = now 
    if i==N-1:
        end = now 

def can_make(arr, distance, C):
    now = arr[0]
    num = 1 
    for i in range(1, len(arr)):
        if arr[i]-now >= distance:
            now=arr[i]
            num += 1 
        if num == C:
            return True 
    return False

# def binary_search(start, end, mid, arr, C, answer):
#     if start > end:
#         return answer 
#     mid = (start + end) // 2 
#     if can_make(arr, mid, C):
#         answer = max(answer, mid)
#         return binary_search(start+1, end, mid, arr, C, answer)
#     else: 
#         return binary_search(start, end-1, mid, arr, C, answer)

def binary_search(arr, C, start, end):
    answer = 0 
    while start <= end:
        mid = (start+end)//2 
        if can_make(arr, mid, C):
            answer = max(answer, mid)
            start = mid+1 
        else:
            end = mid-1 
    return answer

home.sort()
print(binary_search(home, C, 0, end-start))