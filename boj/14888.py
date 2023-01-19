# import sys 
# from itertools import permutations

# input = sys.stdin.readline 

# N = input().rstrip()
# numbers = list(map(int, input().split()))
# operand_num = list(map(int, input().split()))
# operand_list = []
# for i in range(len(operand_num)):
#     for j in range(operand_num[i]): operand_list.append(i)

# def calculate(f, s, oper):
#     if oper == 0:
#         return f+s 
#     elif oper == 1:
#         return f-s
#     elif oper == 2:
#         return f*s 
#     else: 
#         if f<0:
#             if s<0:
#                 return abs(f)//abs(s)
#             else:
#                 return -1* (abs(f)//s)
#         else:
#             if s<0:
#                 return -1 * (f // abs(s))
#         return f//s

# def solution(numbers, opers):
#     oper_idx = 0 
#     ret = numbers[0] 
#     for i in range(1, len(numbers)):
#         ret = calculate(ret, numbers[i], opers[oper_idx])
#         oper_idx += 1 
#     return ret 

# max_answer = 0
# min_answer = 0 
# is_first = True 
# for p in permutations(operand_list, len(operand_list)):
#     val = solution(numbers, list(p))
#     if is_first:
#         max_answer = val 
#         min_answer = val 
#         is_first = False
#     else: 
#         max_answer = max(max_answer, val)
#         min_answer = min(min_answer, val)
# print(max_answer, min_answer)

import sys 

input = sys.stdin.readline 

N = int(input().rstrip())
numbers = list(map(int, input().split()))

a, s, m, d = map(int, input().split())
min_val = 987654321
max_val = -987654321

def dfs(numbers, ret, opers, idx):
    if idx == len(numbers):
        global min_val, max_val 
        min_val = min(ret, min_val)
        max_val = max(ret, max_val)
    else: 
        a,s,m,d = opers
        if a>0:
            a-= 1
            dfs(numbers, ret+numbers[idx], [a,s,m,d], idx+1)
            a+= 1 
        if s>0:
            s-= 1
            dfs(numbers, ret-numbers[idx], [a,s,m,d], idx+1)
            s+= 1 
        if m>0:
            m-= 1
            dfs(numbers, ret*numbers[idx], [a,s,m,d], idx+1)
            m+= 1 
        if d>0:
            d-= 1
            dfs(numbers, int(ret/numbers[idx]), [a,s,m,d], idx+1)
            d+= 1 
dfs(numbers, numbers[0], [a,s,m,d], 1)
print(max_val)
print(min_val)