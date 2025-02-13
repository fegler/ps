import sys 

input = sys.stdin.readline

N = int(input())
number_list = list(map(int, input().split()))
search_number = int(input())

print(number_list.count(search_number))