def solution(gems):
    answer = [0,len(gems)-1]
    size = len(set(gems))
    s,e = 0,0
    gdict = {gems[0] : 1}

    while s < len(gems) and e < len(gems):
        if len(gdict) == size:
            if e-s < answer[1]-answer[0]:
                answer[1] = e
                answer[0] = s
            else:
                gdict[gems[s]] -= 1
                if gdict[gems[s]] == 0 :
                    del gdict[gems[s]]
                s += 1
        else:
            e += 1

            if e == len(gems): break
            if gems[e] in gdict:
                gdict[gems[e]] += 1
            else:
                gdict[gems[e]] = 1

    return [answer[0]+1, answer[1]+1]
