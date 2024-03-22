from collections import deque
from copy import deepcopy
def solution(picks, minerals):
    global answer
    answer = 21e8
    dfs(picks[0],picks[1],picks[2],0,minerals)
    
    return answer

def dfs(dia, iron, stone, now, nowminerals):
    global answer
    if answer <= now : return
    if dia == 0 and iron == 0 and stone == 0 :
        answer = min(now,answer)
        print(answer,dia,iron,stone,nowminerals)
        return
    
    if dia != 0 :
        if len(nowminerals) > 5:
            dfs(dia-1,iron,stone,now+5, nowminerals[5:])
        else :
            answer = min(answer,now + len(nowminerals))
            print(answer,dia-1,iron,stone, nowminerals,'0')
    if iron != 0 :
        if len(nowminerals) > 5:
            tmp = 0
            for i in range(5):
                if nowminerals[i] == 'diamond':
                    tmp += 5
                else : tmp += 1
            dfs(dia,iron-1,stone,now+tmp, nowminerals[5:])
        else :
            tmp = 0
            for mineral in nowminerals:
                if mineral == 'diamond':
                    tmp += 5
                else : tmp += 1
            answer = min(answer, now + tmp)
            print(answer,dia,iron-1,stone,nowminerals,'1')
    if stone != 0 :
        if len(nowminerals) > 5 :
            tmp = 0
            for i in range(5):
                if nowminerals[i] == 'diamond':
                    tmp += 25
                elif nowminerals[i] == 'iron':
                    tmp += 5
                else : tmp += 1
            dfs(dia,iron,stone-1, now+tmp, nowminerals[5:])
        else :
            tmp = 0
            for mineral in nowminerals:
                if mineral == 'diamond':
                    tmp += 25
                elif mineral == 'iron':
                    tmp += 5
                else : tmp += 1
            answer = min(answer, now+tmp)
            print(answer,dia,iron,stone-1,nowminerals,'2')

    