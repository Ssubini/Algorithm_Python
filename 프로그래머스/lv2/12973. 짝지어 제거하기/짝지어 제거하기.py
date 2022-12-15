def solution(s):
    strstack = []
    
    for ss in s:
        if len(strstack) == 0 or strstack[-1] != ss:
            strstack.append(ss)
        else :
            strstack.pop()
            
    if len(strstack) == 0 :
        return 1
    else :
        return 0
