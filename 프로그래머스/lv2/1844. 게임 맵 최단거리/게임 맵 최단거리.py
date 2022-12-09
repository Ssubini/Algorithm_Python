from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    visit = [[0]*m for _ in range(n)]
    
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q : 
        nowy, nowx = q.popleft()
        
        if nowy == n-1 and nowx == m-1 :
            break
        
        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m : continue
            if maps[ny][nx] == 0 : continue
            if visit[ny][nx] != 0 : continue
            visit[ny][nx] = visit[nowy][nowx] + 1
            q.append([ny,nx])
    
    if visit[n-1][m-1] == 0 :
        answer = -1
    else :
        answer = visit[n-1][m-1]
    
    return answer