import sys 

s = sys.stdin.readline().strip()
count_list = [0 for _ in range(ord('a'), ord('z')+1)]

for ss in s:
    count_list[ord(ss)-ord('a')] += 1

for i in range(len(count_list)):
    print(count_list[i], end=' ')