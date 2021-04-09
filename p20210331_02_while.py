#반복문: while
#조건이 참(true)일 동안 실행
# while True:
#     print('python') #무한 실행
#1부터 10까지 출력
#1)
a=0
while True:
    a+=1
    if a>10: break
    print(a)
#2)
a=0
while a<10: #a가 10이 되면 종료된다
    a+=1
    print(a)

#실습) 1~10까지 합을 출력
s=0 #합계를 누적할 변수
a=0 #증가하는 변수
while True:
    a+=1
    if a>10: break
    s+=a
print(s)

#a가 증가하면서 누적합계를 구하고 그 합계가 2000이 넘으면 종료한다
#1)
s=0 #합계를 누적할 변수
a=0 #증가하는 변수
while True:
    a+=1
    s+=a
    if s>2000:
        print(a, s)
        break
#2)
s=0
a=0
while s<2000:
    a+=1
    s+=a
print(a, s)

#사용자가 입력한 수를 누적하다가
#만약 0을 입력하면 반복문 누적합계를 출력
#1)
# s=0
# while True:
#     a=int(input('숫자입력:'))
#     if a == 0:
#         break
#     s+=a
# print(s)
#2)
# s=0
# while a>0:
#     a=int(input('숫자입력:'))
#     s+=a
# print(s)
s=0
a=1
while a!=0:
    a=int(input('숫자입력:'))
    s+=a
print(s)