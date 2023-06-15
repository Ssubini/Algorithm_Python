S = list(input())
z = S.count('0') // 2
o = S.count('1') // 2

for i in range(z):
    S = S[::-1]
    S.remove('0')
    S = S[::-1]

for i in range(o):
    S.remove('1')

print(''.join(S))