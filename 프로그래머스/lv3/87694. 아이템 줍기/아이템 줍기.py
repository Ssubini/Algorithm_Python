from collections import deque

dx = [0, 1, 0, -1, -1, 1, -1, 1]
dy = [1, 0, -1, 0, -1, -1, 1, 1]
dx2 = [0,1,0,-1]
dy2 = [1,0,-1,0]

def checkZero(y,x) :
    for idx in range(8):
        ny = y + dy[idx]
        nx = x + dx[idx]

        if ny < 0 or ny >= 102 or nx < 0 or nx >= 102 : continue
        if board[ny][nx] == 0 :
            return True

    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    global board
    board = [[0]*102 for _ in range(102)]
    check = [[-1]*102 for _ in range(102)]

    for rec in rectangle :
        for i in range(rec[1]*2, rec[3]*2+1):
            for j in range(rec[0]*2, rec[2]*2+1):
                board[i][j] = 1

    q = deque()
    q.append([characterY*2,characterX*2])
    check[characterY*2][characterX*2] = 0

    while q:
        nowy, nowx = q.popleft()
        if nowx == itemX*2 and nowy == itemY*2 :
            return check[nowy][nowx]

        for idx in range(4):
            ny = nowy + dy2[idx]*2
            nx = nowx + dx2[idx]*2
            dny = nowy + dy2[idx]
            dnx = nowx + dx2[idx]

            if ny < 0 or ny >= 102 or nx < 0 or nx >= 102 : continue
            if check[ny][nx] != -1 : continue
            if board[ny][nx] != 1 : continue
            if board[dny][dnx] != 1 : continue
            if checkZero(ny,nx) and checkZero(dny,dnx):
                q.append([ny,nx])
                check[ny][nx] = check[nowy][nowx] + 1
                check[dny][dnx] = check[nowy][nowx] + 1
