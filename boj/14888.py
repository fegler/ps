import sys 
from itertools import permutations

input = sys.stdin.readline 

N = input().rstrip()
numbers = list(map(int, input().split()))
operand_num = list(map(int, input().split()))
operand_list = []
for i in range(len(operand_num)):
    for j in range(operand_num[i]): operand_list.append(i)

def calculate(f, s, oper):
    if oper == 0:
        return f+s 
    elif oper == 1:
        return f-s
    elif oper == 2:
        return f*s 
    else: 
        if f<0:
            if s<0:
                return abs(f)//abs(s)
            else:
                return -1* (abs(f)//s)
        else:
            if s<0:
                return -1 * (f // abs(s))
        return f//s

def solution(numbers, opers):
    oper_idx = 0 
    ret = numbers[0] 
    for i in range(1, len(numbers)):
        ret = calculate(ret, numbers[i], opers[oper_idx])
        oper_idx += 1 
    return ret 

max_answer = 0
min_answer = 0 
is_first = True 
for p in permutations(operand_list, len(operand_list)):
    if p == (1,3,0,0,2):
        print("tmp")
    val = solution(numbers, list(p))
    if is_first:
        max_answer = val 
        min_answer = val 
        is_first = False
    else: 
        max_answer = max(max_answer, val)
        min_answer = min(min_answer, val)
print(max_answer, min_answer)