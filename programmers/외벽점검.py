from itertools import permutations

def solution(n, weak, dist):
    fix_num = len(weak)
    for i in range(len(weak)): 
        weak.append(n+weak[i])
    answer = len(dist)+1
    for i in range(fix_num): ## start point
        for p in permutations(dist, len(dist)):
            num = 1
            next_pos = weak[i]+p[num-1]
            for j in range(i, i+fix_num):
                if weak[j] > next_pos:
                    num += 1 
                    if num > len(dist):
                        num = -1
                        break 
                    else: 
                        next_pos = weak[j] + p[num-1]
            if num != -1:
                answer = min(answer, num)
    if answer > len(dist):
        answer = -1
    return answer 

print(solution(12, [1,3,4,9,10], [3,5,7]))