def solution(s):
    answer = 0
    for i in range(len(s)):
        check = []
        flag = 0
        for j in range(len(s)):
            if s[(i+j)%len(s)] == '(' or s[(i+j)%len(s)] == '[' or s[(i+j)%len(s)] == '{' :
                check.append(s[(i+j)%len(s)])
            elif len(check) == 0 :
                flag = 1
                break
            elif check[-1] == '(' :
                if s[(i+j)%len(s)] == ')' :
                    check.pop()
                else:
                    flag = 1
                    break
            elif check[-1] == '{':
                if s[(i+j)%len(s)] == '}':
                    check.pop()
                else :
                    flag = 1
                    break
            elif check[-1] == '[':
                if s[(i+j)%len(s)] == ']':
                    check.pop()
                else :
                    flag = 1
                    break
            
        if len(check) != 0 or flag == 1 : continue
        else : answer += 1
    
    return answer