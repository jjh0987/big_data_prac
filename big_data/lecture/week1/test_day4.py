result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

class calculator:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    def sub(self,num):
        self.result -= num
        return self.result

cal1 = calculator()
cal2 = calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class cookie:
    pass
a = cookie()
type(a)

class fourcal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

a = fourcal()
fourcal.setdata(a,4,2) == a.setdata(4,2)

a.setdata(4,2) # self : a
#print(a.first)
#print(a.second)
#print(a.add(a.first,a.second))

b = fourcal()
b.setdata(3,7)
print(b.first)
b.add()


class fourcal:
    def __init__(self,first,second): # class 인풋 변수
        self.a = first # class 안에서 사용될 변수
        self.b = second

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

x = fourcal(4,2)
x.add()

class fourcal_pickle(fourcal):
    def pow(self):
        return self.a ** self.b
    def div(self):
        if self.b == 0:
            return 'err'
        else:
            return self.a / self.b
a = fourcal_pickle(2,0)
a.add()
a.pow()
a.div() # 피클된 클래스에서 역으로 수정 가능 : 클래스 오버라이딩

class family:
    lastname = 'kim'
print(family.lastname)
family.lastname = 'park'
print(family.lastname) # 배리어블 오버라이딩

from mod import mod1
a = mod1.add(1, 2)
mod1.fourcal_pickle(1, 0).add()
a = mod1.test.test1.test2()
print(a.add(1,2))
b = mod1.tet()
print(b.add(1,2))

from mod.mod1 import fourcal_pickle,test
a = add(1, 2)
fourcal_pickle(1, 0).add()
a = test.test1.test2()
print(a.add(1,2))
b = tet()
print(add(1,2))

try:
    age = int(input())
except:
    print('none')
else:
    if age <= 18:
        print('warn')
    else:
        print('welcome')

class bird:
    def fly(self):
        raise NotImplemented
class eagle(bird):
    pass
x = eagle()
x.fly() # 이글에서 fly를 구현하게 만듬

class eagle(bird):
    def fly(self):
        print('fast')
x = eagle()
x.fly()

all([1,2,3])
all([1,2,3,0]) # 하나라도 거짓이면 false
any([1,2]) # 하나만 참이면 true