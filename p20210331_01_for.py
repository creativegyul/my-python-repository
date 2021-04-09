#반복문: for 반복적으로 수행해야 할 일이 있을때
#for 변수 in 범위: 범위 만큼 반복적으로 실행
for x in [1,2,3,4,5]:
    print('python')
data=[1,20,30,7,9]
for x in data:
    print('python', x)

# data=['몽실','쿠키','꽃님']
# for x in data:
#     print(x)
# for x in [0,1,2]:
#     print(data[x])
# print(data[0])
# print(data[1])
# print(data[2])

#실습) 0~9 출력
# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x)
# print(list(range(10,51,2))) #range(start,stop,step) range: 정수를 생성(실수x)
# print(list(range(101))) #0, step 1 생략가능
# print(list(range(10,20))) #start,stop
# for x in range(0,10,2):
#     print(x)

#합계를 구하기
#1부터 10까지 출력
s=0 #합계를 저장할 변수
for x in range(1,11):
    s+=x #s = s+x
print(s)

#실습) 사용자에게 숫자를 입력받아 1부터 그 수까지 더하기
s=int(input('숫자입력:'))
for x in range(1,s):
    s+=x
print(s)

s=0
last=int(input('숫자입력:'))
for x in range(1,last+1):
    s+=x
print(s)

#실습) 1부터 100까지 합이 2000이 넘을때 그 수를 출력
s=0
for x in range(1,101):
    s+=x
    if s>2000:
        break #반복문을 종료할때 사용하는 keyword
print('x =',x,'s =',s)

#실습) 바보라는 글자가 발견되면 강퇴
data=['안녕','반가워','방가','하이','잘가']
bad=['바보','멍청이']
for x in data:
    print(x)
    if x in bad:
        print('강퇴')
        break
else: #for문이 정상수행했다면(break문을 실행하지 않았다면)
    print('바른말 사용자')

#continue
data=[3,4,6,8,7,10]
for x in data:
    if x%2==1: continue #다음작업을 진행하지 않고 for문으로 돌아가기
    print(x)

#실습) 어떤 학생의 점수리스트가 주어졌을 때, 모든 점수가 60점이 넘으면 합격하는 프로그램
# score=[65,45,95,55,70]
# score=input('점수는?').split() #() 공백으로 분류
# score=map(int,score)
# # print(list(score))
# for x in score:
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

#실습) 어떤 학생의 점수리스트가 주어졌을 때, 모든 점수의 합계가 300이 넘으면 합격하는 프로그램
s=0
score=[65,45,95,55,70]
for x in score:
    s+=x
    if s>300:
        print('합격')
        break
else:
    print('불합격')