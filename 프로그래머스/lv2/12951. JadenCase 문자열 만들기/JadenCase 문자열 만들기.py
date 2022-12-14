def solution(s):
    answer = ''
    for idx in range(len(s)):
        if idx == 0 or s[idx-1] == ' ':
            if 'a' <= s[idx] <= 'z':
                answer += chr(ord(s[idx])-ord('a')+ord('A'))
            else :
                answer += s[idx]
        else :
            if 'A' <= s[idx] <= 'Z':
                answer += chr(ord(s[idx])-ord('A')+ord('a'))
            else :
                answer += s[idx]
        
    return answer