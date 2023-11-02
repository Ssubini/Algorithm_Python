import sys
from collections import deque
input = sys.stdin.readline

S = int(input())
screan = 1
cboard = 0
cnt = 0

q = deque()
q.append([screan, cboard, cnt])
visit = [[False]*(S*2+1) for _ in range(S+1)]

while q:
    nowscrean, nowcboard, cnt = q.popleft()
    if nowscrean == S:
        print(cnt)
        break

    if nowscrean >= S*2 or nowcboard >= S: continue
    if visit[nowcboard][nowscrean] : continue

    # 복사
    q.append([nowscrean, nowscrean, cnt+1])

    # 붙여넣기
    if nowcboard != 0 :
        q.append([nowscrean+nowcboard, nowcboard, cnt+1])

    # 삭제
    if nowscrean != 0:
        q.append([nowscrean-1, nowcboard, cnt+1])

    visit[nowcboard][nowscrean] = True