#조건문
a=-10 #참 or 거짓
if a>0: #참
    print('양수')
    print(a)
else: #거짓
    print('음수')
    print(a)

#실습) 회원등급 출력
#a가 90보다 크면 good 아니면 try 출력
# a=int(input('숫자입력:'))
# if a>90:
#     print('good')
# else:
#     print('try')

#실습) 비밀번호 체크
#기존 비밀번호와 일치하면 '문이 열립니다' 일치하지 않으면 '다시 확인하세요'
# pw='1234' #기존 비밀번호
# a=input('비밀번호는?')
# if a==pw:
#     print('문이 열립니다')
# else:
#     print('다시 확인하세요')

#어떤 수가 짝수이면 '짝수' 홀수이면 '홀수' 출력
# a=int(input('숫자입력:'))
# if a==0:
#     print('짝수도 홀수도 아님')
# elif a%2==0:
#     print('짝수')
# else:
#     print('홀수')

#실습) ~90점 A, 80~89점 B, 70~79점 C, 60~69점 D, ~59점 F
# a=int(input('점수:'))
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')

#실습) 키와 몸무게를 입력받아서 비만여부를 출력
h=int(input('키:'))
w=int(input('몸무게:'))
p=(h-100)*0.9
a=p*0.95
b=p*1.05
if w>b:
    print('비만')
elif w>=a:
    print('정상체중')
elif w<a:
    print('저체중')

# weight=60.1
# height=165.5
# normal=(height-100)*0.9
# print('정상체중:',normal)
# if weight < normal*0.95:
#     print('미달')
# elif weight <= normal*1.05:
#     print('정상')
# else:
#     print('비만')

#실습) 계산기
#두 수와 기호를 입력받아 사칙연산
x=int(input('첫번째 숫자:'))
y=int(input('두번째 숫자:'))
z=input('사칙연산기호:')
if z=='+':
    print('%d + %d = %d' %(x, y, x+y))
elif z=='-':
    print('%d - %d = %d' %(x, y, x-y))
elif z=='*':
    print('%d * %d = %d' %(x, y, x*y))
elif z=='/':
    print('%d / %d = %.2f' %(x, y, x/y))
else:
    print('잘못된 기호')

#2)
# data=input('계산식은?').split()
# a=int(data[0])
# b=int(data[2])
# if b=='+':
#     print(a+c)
'''
#2)
# data=input('계산식은?').split()
# a=int(data[0])
# b=int(data[2])
# sign=data[1]
# if sign=='+':
#     print('%d + %d = %d'%(a,b,a+b))
# elif sign == '-':
#     print('%d - %d = %d'%(a,b,a-b))
# elif sign == '*':
#     print('%d * %d = %d'%(a,b,a*b))
# elif sign == '/':
#     print('%d / %d = %d'%(a,b,a/b))
# else:
#     print('잘못된 기호')

# 3)eval은 강력하지만 보안에 취약, 주의
import os
# print(os.listdir())
# data = input('계산식은?')
# print(eval(data))

#실습)두수를 입력을 받아서 큰수를 화면에 출력
# a=int(input('first?'))
# b=int(input('second?'))
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print('두수는 같다')

#실습)거스름돈계산
# amount = int(input('물품금액:'))
# pay = int(input('낸금액:'))
# if pay>amount:
#     print('거스름돈:', pay-amount)
# elif pay<amount:
#     print('부족금액:', amount-pay)
# else:
#     print('계산완료')

#논리연산자
# a=10;b=20
# print(a>0 and b>0)
# print(a>0 and b<0)
# print(a>0 or b<0)
# print(not (a>0))
# a=-10; b=10
# if a==0 or b==0:
#     print('0이 아닌수를 입력하세요')
# elif a>0 and b>0:
#     print('둘다 양수')
# elif a>0 or b>0:
#     print('둘중에 하나가 음수')
# else:
#     print('둘다 음수')
'''

price={'1':['자장면',5000,'중식'],'2':['짬뽕',6500,'중식'],'3':['설렁탕',8000,'한식'],'4':['비빔밥',8500,'한식'],'5':['피자',12000,'양식'],'6':['스파게티',10500,'양식']}
print('-' * 22)
print('[국제식당]오늘의 메뉴')
print('-' * 22)
print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
print('-' * 15)
no = input('메뉴는?')
menu=price.keys()
if no in menu:
    print(price[no][0], '선택')
    print(price[no][1], '원')
    print(price[no][2], '코너')
else:
    print('잘못 입력하셨습니다.')
# if no in ['1','2']: #in: 포함 여부
#     print('중식코너')
# elif no in ['3','4']:
#     print('한식코너')
# elif no=='5' or no=='6':
#     print('양식코너')
# else:
#     print('잘못 입력하셨습니다.')