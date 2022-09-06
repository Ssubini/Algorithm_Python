from collections import deque
def regD(num):
    return (num*2)%10000

def regS(num):

    if num == 0:
        ret = 9999
    else :
        ret = num - 1

    return ret

def regL(num):
    sn = str(num)
    nsn = ''
    for i in range(4-len(sn)):
        nsn += '0'
    nsn += sn

    rsn = nsn[1:] + nsn[0]

    return int(rsn)

def regR(num):
    sn = str(num)
    nsn = ''
    for i in range(4 - len(sn)):
        nsn += '0'
    nsn += sn
    rsn = nsn[-1]+nsn[:3]

    return int(rsn)


T = int(input())
for tc in range(T):
    A,B = map(int,input().split())

    q = deque()
    q.append([A,0,''])
    visit = [0]*10000

    while True:

        nowA, level, answer = q.popleft()
        visit[nowA] = 1

        if nowA == B :
            print(answer)
            break

        for i in range(4):
            if i == 0 :
                tmp = regD(nowA)
                if visit[tmp] == 0 :
                    q.append([tmp,level+1,answer+'D'])
                    visit[tmp] = 1

            elif i == 1 :
                tmp = regS(nowA)
                if visit[tmp] == 0:
                    q.append([tmp,level+1,answer+'S'])
                    visit[tmp] = 1

            elif i == 2 :
                tmp = regL(nowA)
                if visit[tmp] == 0:
                    q.append([tmp,level+1,answer+'L'])
                    visit[tmp] = 1

            elif i == 3 :
                tmp = regR(nowA)
                if visit[tmp] == 0:
                    q.append([tmp,level+1,answer+'R'])
                    visit[tmp] = 1
