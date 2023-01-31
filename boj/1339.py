import sys 

input = sys.stdin.readline 
N = int(input().strip())

str_list = [] 
word_list = []

for _ in range(N):
    row = input().strip()
    word_list.append(row)
    str_list += list(set(row))
str_list = list(set(str_list))

weight_dict = {i: 0 for i in str_list}
for word in word_list:
    l = len(word)
    for i in range(l):
        weight_dict[word[i]] += 10 ** (l-i)

weight_list = list(weight_dict.items())
weight_list.sort(key=lambda x: -x[1])
mapping_dict = {i: -1 for i in str_list}
now = 9
for w in weight_list:
    mapping_dict[w[0]] = now 
    now -= 1 

answer = 0 
for word in word_list: 
    l = len(word)
    for i in range(l):
        answer += (mapping_dict[word[i]] * (10 ** (l-i-1)))
print(answer)
