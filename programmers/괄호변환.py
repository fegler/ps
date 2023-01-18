
def split_str(p):
    left_num, right_num = 0, 0
    left= ''
    for i in range(len(p)):
        if p[i] == '(':
            left_num += 1
        else:
            right_num += 1 
        left += p[i]
        if left_num == right_num:
            if i == len(p)-1:
                return left, ''
            else:
                return left, p[i+1:]

def check_correct(p):
    left_num = 0
    for i in p:
        if i == '(':
            left_num += 1 
        else: 
            if left_num > 0:
                left_num -= 1 
            else:
                return False 
    if left_num > 0:
        return False 
    return True 

def reverse_str(p):
    ret = '' 
    for i in p:
        if i == '(':
            ret += ')'
        else:
            ret += '('
    return ret 

def recur_func(p):
    if len(p)==0: return ''

    u, v = split_str(p)
    if check_correct(u):
        return u + recur_func(v)
    else: 
        return '(' + recur_func(v) + ')' + reverse_str(u[1:-1])

def solution(p):
    return recur_func(p)

print(solution("()))((()"))
