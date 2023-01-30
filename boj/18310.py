import sys
input = sys.stdin.readline 

N = int(input().rstrip())

home = list(map(int, input().split()))
home.sort()
print(home[len(home)//2] if len(home)%2!=0 else home[len(home)//2 - 1])