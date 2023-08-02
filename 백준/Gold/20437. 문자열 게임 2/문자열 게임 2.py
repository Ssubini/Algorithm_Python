from collections import defaultdict
T = int(input())
for t in range(T):
    W = input()
    K = int(input())
    answer = []

    counts = defaultdict(int)

    for w in W :
        counts[w] += 1

    check = False
    max_answer = -1
    min_answer = len(W)

    check_dict = defaultdict(list)

    for i in range(len(W)):
        if counts[W[i]] < K : continue
        check = True
        check_dict[W[i]] += [i]

    for key, value in check_dict.items():
        for i in range(len(value)-K+1):
            max_answer = max(max_answer, value[i+K-1]-value[i]+1)
            min_answer = min(min_answer, value[i+K-1]-value[i]+1)

    if check:
        print(min_answer, max_answer)
    else:
        print(-1)
