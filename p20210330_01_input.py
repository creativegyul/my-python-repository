#사용자에게 입력받기
# a=input('입력하세요 ')
# print('입력한 값은',a)

#실습) 나이를 입력받아 화면에 출력
#입력한 값은 문자 취급
# a=input('당신의 나이는?(숫자만)\n')
# print(a,'세',sep='')

# age=input('나이는? ')
# print('당신의 나이는 '+age+'세 입니다.')

#예) 오늘의 날씨는 맑음
# txt='오늘의 날씨는\n'
# a=input(txt)
# print('오늘의 날씨는',a*2)

# txt='오늘의 날씨는'
# w=input('날씨:')
# print(txt,w,sep=':')

#help(print) #print함수의 도움말 출력.
#사용자가 입력한 값에 100을 더해서 출력
# a=input('숫자는?')
# a=int(a) #정수로 변환해서 반환해주는 함수
# a=float(a) #실수로 변환해서 반환해주는 함수
# print(a+100)

#실습) 사용자에게 두 수를 입력받아 사칙연산 프로그램
# x=input('첫번째 숫자를 입력하세요\n')
# y=input('두번째 숫자를 입력하세요\n')
# x=float(x)
# y=float(y)
# print('%.1f + %.1f = %.1f' %(x,y,x+y))
# print('%.1f - %.1f = %.1f' %(x,y,x-y))
# print('%.1f * %.1f = %.1f' %(x,y,x*y))
# print('%.1f / %.1f = %.1f' %(x,y,x/y))

# a=int(input('첫번째수?'))
# b=int(input('두번째수?'))
# print('%d+%d=%d'%(a,b,a+b))
# print('두 수를 더한 값은',(a+b),'입니다')

#2)
# data=input('두 수는?')
# a=int(data.split()[0])
# b=int(data.split()[1])
# print(a,'+',b,'=',a+b)

# data=input('두 수는?').split() #두 수를 분리.
# a,b = map(int, data) #data의 각 값을 int함수를 적용한 후 a,b에 대입
# print(a,'+',b,'=',a+b)

#실습) 반지름을 사용자로부터 입력받아 원의 넓이 구하기(원주율 3.14)
a=int(input('반지름의 길이는? '))
b=(a*a)*3.14
print('원의 넓이는',b,'입니다')

r=float(input('반지름:'))
print('원의 넓이는', r**2 * 3.14) #**2 제곱 ***3 세제곱