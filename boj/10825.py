from functools import cmp_to_key
import sys 

input = sys.stdin.readline 

N = int(input().rstrip())


## compare function 
# def func(data1, data2):
#     na, ko, en, ma = data1 
#     na2, ko2, en2, ma2 = data2 
#     if ko != ko2:
#         return 1 if ko < ko2 else -1 
#     elif en != en2:
#         return 1 if en > en2 else -1 
#     elif ma != ma2:
#         return 1 if ma < ma2 else -1 
#     else: 
#         return 1 if na > na2 else -1 

student = [] 
for _ in range(N):
    na, ko, en, ma  = input().split()
    student.append([na, int(ko), int(en), int(ma)])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0])) ## lambda function ver. 
# student.sort(key=cmp_to_key(func))
for i in student: 
    na, _, _, _ = i 
    print(na)
