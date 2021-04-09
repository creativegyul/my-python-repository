#연습문제
#1)별찍기 1번
# print('*'*1)
# print('*'*2)
# print('*'*3)
# print('*'*4)
# print('*'*5)
# print('*'*6)

for x in range(1,7):
    print('☆'*x)

#별찍기 2번
for x in range(6,0,-1):
    print('*'*x)

#별찍기 3번
# print('☆'*5,'*'*1, sep='')
# print('☆'*4,'*'*2, sep='')
# print('☆'*3,'*'*3, sep='')
# print('☆'*2,'*'*4, sep='')
# print('☆'*1,'*'*5, sep='')
# print('*'*6)

# print(' ' * 5, end=''); print('★' * 1)
# print(' ' * 4, end=''); print('★' * 2)
# print(' ' * 3, end=''); print('★' * 3)
# print(' ' * 2, end=''); print('★' * 4)
# print(' ' * 1, end=''); print('★' * 5)
# print(' ' * 0, end=''); print('★' * 6)
'''
for z in range(1,7):
    for x in range(6-1):
    print('0'*x, end='')
    for y in range(1,7):
        print('★'*y, end='')
    print()
'''
#실습2) 구구단을 출력하는 프로그램
#예) 2 * 1 = 2
#   2 * 2 = 4
#   2 * 3 = 6
for x in range(1,10):
    print('2 * %d = %d' %(x,2*x))

# dan=int(input('몇단?'))
# for x in range(1,10):
#     print('%d * %d = %d' %(dan,x,dan*x))
'''
#2~9단까지 출력

for x in range(1,10):
    for y in range(1, 10): #x가 1일때 y값은 1씩 증가되면서 총 9번 실행 (9*9=81)
        print(x,y)
'''
#실습3) 숫자를 입력받아 그 범위 안의 수 중 0부터 3의 배수를 출력하는 프로그램
#예) 0 3 6 9 12 15 18 ...30
# a=int(input('숫자입력:'))
# for x in range(0,a+1,4):
#     print(x,end=' ')
# print()
# for x in range(0,a+1):
#     if x%3==0:
#         print(x, end=' ')
# print()

#실습4) 숫자 두 개와 기호를 입력받아 계산기 프로그램 만들기, 단 q를 입력하면 프로그램 종료
#반복
#1) 두 수와 기호를 입력받는다
#2) 기호에 따라 계산
#3) 계속진행여부 입력
while True:
    a=input('시작하려면 숫자입력/종료하려면 q:')
    if a == 'q': break
    a=int(a)
    b=int(input('두번째 숫자:'))
    #원하는 기호가 입력될때까지 계속 입력
    while True:
        c=input('연산기호:')
        if c in ['+','-','*','/']: break
    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)
    else:
        print('잘못된 기호')
    if input('종료(y)?')=='y': break

#실습3) 학생들의 점수가 딕셔너리로 저장되어 있을 때 값이 90점 이상인 학생들의 key만 출력하시오
#예시) dicA={1:94,2:87,3:91,4:75,5:92}
#출력) 90점 이상 학생
#       1번
#       3번
#       5번
dic={1:94,2:87,3:91,4:75,5:92}
print(dic.keys())
print(dic.values())
print(dic.items())
for no,score in dic.items():
    if score>=90:
        print(no,'번',sep='')

#실습6) listA=['쿠키','꽃님','초코','몽실'] 판매수량을 입력받아 히스토그램을 그리는 프로그램
#출력 예) 쿠키:*********
#         꽃님:************
#         초코:*******
#         몽실:*****
#1) 사원의 판매수량 입력
#2) 히스토그램 그리기
#데이터구조: {'쿠키':10,'꽃님':15,'초코':5,'몽실':7}
list=['쿠키','꽃님','초코','몽실']
qty={} #판매수량을 저장할 딕셔너리
for name in list:
    qty[name]=int(input(name+'?'))
for name,star in qty.items():
    print(name,':',star*'*',sep='')

#실습 7) 적정체중 구하기-이름/신장/몸무게를 입력 받고 적정체중 여부를 출력
# h=int(input('키:'))
# w=int(input('몸무게:'))
# p=(h-100)*0.9
# a=p*0.95
# b=p*1.05
# if w>b:
#     print('비만')
# elif w>=a:
#     print('정상체중')
# elif w<a:
#     print('저체중')