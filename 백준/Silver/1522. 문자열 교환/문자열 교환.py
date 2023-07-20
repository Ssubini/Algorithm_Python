s = input()
total = s.count('a')
s += s[0:total-1]
start = s[0:total].count('b')
answer = start
for i in range(total,len(s)):
    if s[i-total] == 'b':
        start -= 1
    if s[i] == 'b':
        start += 1
    answer = min(answer,start)
    # print(answer)

print(answer)