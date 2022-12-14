def bn(num):
    answer = ''
    while num != 0:
        answer += str(num % 2) 
        num //= 2
    return answer[::-1]

def solution(s):
    answer = []
    cnt = 0
    zeros = 0
    
    while True:
        if s == '1': break
        cnt += 1
        ns = ''
        for ss in s:
            if ss == '0':
                zeros += 1
            else :
                ns += ss
        
        tmp = len(ns)
        s = bn(tmp)
    
    answer = [cnt,zeros]
    
    return answer