#모듈 *라이브러리에 저장돼있는 모듈
import time
print(time.localtime().tm_year,'년', sep='', end=' ')
print(time.localtime().tm_mon,'월', sep='', end=' ')
print(time.localtime().tm_mday,'일', sep='')
print(time.localtime().tm_hour,'시',time.localtime().tm_min,'분',time.localtime().tm_sec,'초')

from datetime import datetime as d
now=d.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))

sleep 함수: 프로그램 실행 속도를 제어
import time
print('시작')
time.sleep(3)
print('3초 지남')
timer 만들기
from time import sleep
sec=int(input('몇초?'))
print('타이머 시작')
for x in range(1,sec+1):
    sleep(1)
    print(x,'초',sep='')

#calendar 모듈(?)

#난수모듈
#주사위 게임
# print('<주사위 던지기>')
# name=input('이름1:')
# name2=input('이름2:')
# import random
# a=random.randint(1,6)
# b=random.randint(1,6)
# print(name,':',a,',',name2,':',b)
# if a>b:
#     print(name, 'Win')
# elif a<b:
#     print(name2, 'Win')
# else:
#     print('Draw')

'''import random
awin=0 #a이긴 횟수
bwin=0 #b이긴 횟수
while awin==3:
    a=random.randint(1,6)
    b=random.randint(1,6)
    print('A:',a,'B:',b)
    if a>b:
        print('A Win')
    elif b>a:
        print('B Win')
    else:
        print('Draw')
for x in range(1,awin+1): break''' #주사위게임 삼세판???

import random
#sample()
print(random.sample(range(1,46),6))

#choice()
print(random.choice(['가위','바위','보']))

#shuffle(): 섞음
data=['초코','쿠키','딸기','초코','쿠키','딸기']
random.shuffle(data)
print(data)

# import turtle
# turtle.shape('turtle')
# turtle.color('green')
# for x in range(50):
#     turtle.forward(5)
#     turtle.right(5)
# turtle.done()