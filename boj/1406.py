import sys  
from collections import deque
input = sys.stdin.readline

s = input().strip()
M = int(input())

left_stack, right_stack = deque([]), deque([]) 
for ss in s:
    left_stack.append(ss)

for _ in range(M):
    # print(left_stack, right_stack)
    command = input().split()
    if command[0] == 'P':
        left_stack.append(command[1])
    elif command[0] == 'L':
        if len(left_stack) != 0:
            right_stack.appendleft(left_stack.pop())
    elif command[0] == 'D':
        if len(right_stack) != 0:
            left_stack.append(right_stack.popleft())
    elif command[0] == 'B':
        if len(left_stack) != 0:
            left_stack.pop()

left_stack.extend(right_stack)
for i in range(len(left_stack)):
    print(left_stack[i], end='')
# print("".join(left_stack))
# for i in range(len(left_stack)):
#     print(left_stack[i], end='')
# for i in range(len(right_stack)):
#     print(right_stack[i], end='')