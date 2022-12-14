def solution(s):
    answer = True
    check = []
    
    for ss in s:
        if ss == '(':
            check.append(ss)
        else :
            if check:
                check.pop()
            else :
                answer = False
                break
    
    if answer and len(check) == 0 :
        return True
    else :
        return False
