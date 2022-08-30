board = [list(map(int,input().split())) for _ in range(10)]
paper = [5,5,5,5,5]
answer = 26  # 0개 인경우 25x

def paperOn(y,x):
    okpaper = []
    for idx in range(1,6):
        for i in range(y,y+idx):
            for j in range(x,x+idx):
                if i < 0 or i >= 10 or j < 0 or j >= 10 or board[i][j] == 0 :
                    return okpaper
        okpaper.append(idx)
    return okpaper

def color(y,x,size):
    for i in range(y,y+size):
        for j in range(x,x+size):
            board[i][j] = 0

def colorback(y,x,size):
    for i in range(y,y+size):
        for j in range(x,x+size):
            board[i][j] = 1

def dfs(level):
    global answer
    if level == 0:
        answer = min(answer, 25-sum(paper))
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                okpaper = paperOn(i,j)
                for p in okpaper:
                    if paper[p-1] > 0 :
                        paper[p-1] -= 1
                        color(i,j,p)
                        dfs(level - p*p)
                        paper[p-1] += 1
                        colorback(i,j,p)
                return


one = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 1 : one += 1

dfs(one)
if answer == 26 : answer = -1
print(answer)
