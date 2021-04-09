#문자열 다루기
txt = 'python is easy!'
print(txt[0])
print(txt[-1]) #마지막 인덱스
print(txt[7:9]) #start index : stop index
print(txt[:2]) #0:2 (0은 생략가능)
print(txt)
print(txt[:-1])
print(txt[-5:-1])
print(txt[-5:]) #-5부터 끝까지

#실습1
s = 'my house'
print(s[3:])
#실습2
txt="012345678901234567890123456"
print(txt[:10])
print(txt[10:20])
print(txt[20:])