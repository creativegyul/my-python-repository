#class: 객체를 만들기 위한 틀
class Car:
    #속성: 필드
    name='포르쉐'
    color='레드'
    pw=False
    #기능:
    def power(self):
        pw=not Car.pw

c1=Car() #c1: 객체명
print(c1.name)
c1.power()

c2=Car()