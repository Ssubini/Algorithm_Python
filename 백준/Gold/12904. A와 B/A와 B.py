S = input()
T = input()

answer = 0
while True:
    if S == T :
        answer = 1
        break
    elif len(S) > len(T):
        break

    if T[-1] == 'A':
        T = T[:-1]
    else :
        T = T[-2::-1]

print(answer)