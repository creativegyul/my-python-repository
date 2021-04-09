#튜플
# data=(10,20,30,40,50)
data=10,20,30,40,50 #튜플은 소괄호 생략가능.
print(data[0])
# data[1]=200 #변경이 불가능

#두 수를 바꾸기
a=10; b=20
temp=a
a=b
b=temp
print(a,b) #20,10

#패킹과 언패킹
a=10; b=20
b,a=a,b
print(a,b)