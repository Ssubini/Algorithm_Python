def solution(n, words):
    answer = [0,0]
    tmp = []

    for idx in range(len(words)):
        if len(tmp) == 0 :
            tmp.append(words[idx])
        elif words[idx] not in tmp and words[idx-1][-1] == words[idx][0]:
            tmp.append(words[idx])
        else:
            answer = [idx%n+1, idx//n+1]
            break
    
    return answer