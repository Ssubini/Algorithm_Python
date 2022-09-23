import copy


def solution(info, edges):
    global Max, cango, flag
    dic = {}
    
    cango = []
    Max = 1
    
    for pa, ch in edges:
        if pa in dic:
            dic[pa].append(ch)
        else:
            dic[pa] = [ch]
    lenInfo = len(info)
    visit=[0]*lenInfo
    visit[0]=1
    flag=0
    
    def dfs(sh, wo, lo, cango):
        global Max, flag
        
        if wo>=sh:
            return
        for i in range(lenInfo):
            if info[i]==0:
                if visit[i]==0:
                    flag=1
                    break
        if flag==0:
            return
            
        Max=max(Max,sh)
        
        for location in cango:
            if visit[location]==1: continue
            visit[location]=1
            backupcan = copy.deepcopy(cango)
            backupcan.remove(location)
            if location in dic:
                backupcan.extend(dic[location])
                
            if info[location]:
                dfs(sh, wo+1, location, backupcan)
            else:
                dfs(sh+1, wo, location, backupcan)
            visit[location]=0
        

    cango=dic[0]
    dfs(1, 0, 0, cango)
    
    answer = Max
    return answer