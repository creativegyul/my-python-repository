#내장함수 Built-in Function
data=[5,18,4,6] #전역변수: 어떤 함수에서든 가져다 쓸수있는 변수
print(sum(data))

#sum의 사용자함수 정의:
#매개변수: 리스트, 반환값: 합계
def mysum(a):
    s=0
    for x in a:
        s+=x
    return s

r=mysum(data)
print('리턴값:',r)

#max함수
m=max(data)
print('가장 큰 값:',m)
n=min(data)
print('가장 작은값:',n)
#max값 사용자 함수
def mymax(a):
    a=data[0]
    for x in data:
        if x>a:
            a=x
    return a

print('가장 큰 값:', mymax(data))
data=[78,8,5,16]
print('가장 큰 값:', mymax(data))

#min값을 구하는 사용자 함수
def mymin(adata):
    a=adata[0]
    for x in adata:
        if x<a:
            a=x
    return a
data=[5,18,4,6]
r=mymin(data)
print('가장작은값:',r)

#ord() 함수
print(ord('A'),len('A'),'A'.encode(), len('A'.encode())) #ord: 아스키코드값
print(ord('허'),len('허'),'허'.encode(), len('허'.encode())) #한글은 유니코드체계
print(chr(54728))

#실습1) 사칙연산 함수
#매개변수: 두 수, 반환값: 결과
# x=int(input('첫번째수?'))
# y=int(input('두번째수?'))
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
#리턴값은 한개만 가능
def cal(a,b):
    return a+b,a-b #튜플로 반환
x=10
y=5
print('더하기:', add(x,y))
print('빼기:', minus(x,y))
print('계산:', cal(x,y)[0], cal(x,y)[1])

#실습2) 월급 구하기
#매개변수: 연봉, 시급, 초과근무시간, 반환값: 월급
#(월급 = 연봉/12 + 시급*초과근무시간)
def sal(a,b,c):
    return a/12+b*c
y=30000000
s=20000
c=30
print('월급:', sal(y,s,c))