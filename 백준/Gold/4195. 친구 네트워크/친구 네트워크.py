def find(x):
    if arr[x] < 0:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x,y):
    a, b = find(x), find(y)
    if (a!=b):
        arr[a] += arr[b]
        arr[b] = a
    return arr[a]

test_case = int(input())
for test in range(test_case):
    n = int(input())
    names = {}
    cnt = 0
    arr = [-1] * (2*n+2)
    for i in range(n):
        f1, f2 = input().split()
        if f1 not in names:
            names[f1] = cnt
            cnt += 1
        if f2 not in names:
            names[f2] = cnt
            cnt += 1
        print(-1 * union(names[f1], names[f2]))