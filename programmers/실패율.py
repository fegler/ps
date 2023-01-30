def solution(N, stages):
    answer = []
    stages.sort(reverse=True)
    now = N 
    not_clear_num = 0 
    num = 0 
    idx = 0 
    while idx < len(stages):
        val = stages[idx]
        if val < now:
            ## 실패율 계산 
            if num == 0:
                answer.append((0, now))
            else: 
                answer.append((not_clear_num/num, now))
                not_clear_num = 0 
            now -=1 
        else:
            if val == now:
                not_clear_num+=1
            num += 1
            idx += 1
    for i in range(now, 0, -1):
        answer.append((not_clear_num/num, i))
        not_clear_num = 0 
    answer.sort(key=lambda x: (-x[0], x[1]))
    answer = [i[1] for i in answer]
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))