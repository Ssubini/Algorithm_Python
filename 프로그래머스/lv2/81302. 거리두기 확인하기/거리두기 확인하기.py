def check(board):
    dx1 = [0,0,1,-1]
    dy1 = [1,-1,0,0]
    dx2 = [0,0,2,-2]
    dy2 = [2,-2,0,0]
    dx3 = [1,1,-1,-1]
    dy3 = [1,-1,1,-1]
    
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                for idx in range(4):
                    nx = j + dx1[idx]
                    ny = i + dy1[idx]
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 : continue
                    if board[ny][nx] == 'P' : return 0
                for idx in range(4):
                    nx = j + dx2[idx]
                    ny = i + dy2[idx]
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 : continue
                    if board[ny][nx] == 'P':
                        cy = (i+ny)//2
                        cx = (j+nx)//2
                        if board[cy][cx] == 'O': return 0
                for idx in range(4):
                    nx = j + dx3[idx]
                    ny = i + dy3[idx]
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 : continue
                    if board[ny][nx] == 'P':
                        if board[i][nx] == 'O' or board[ny][j] == 'O' : return 0
    return 1


def solution(places):
    answer = []
    for room in places:
        answer.append(check(room))
    return answer