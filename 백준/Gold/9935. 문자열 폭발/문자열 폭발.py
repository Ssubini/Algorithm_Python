import sys
input = sys.stdin.readline

S = input().strip()
del_S = list(input().strip())
l = len(del_S)
last_word = del_S[-1]
answer = []
for i in S:
    answer.append(i)
    if i == last_word and answer[-l:] == del_S:
        for k in range(l):
            answer.pop()
if answer :
    print(''.join(answer))
else :
    print("FRULA")