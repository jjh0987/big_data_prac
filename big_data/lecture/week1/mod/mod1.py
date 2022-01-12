def add(a,b):
    return a+b
def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))

class fourcal:
    def __init__(self,first,second): # class 인풋 변수 , class 호출시 바로 설정
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

class fourcal_pickle(fourcal):
    def pow(self):
        return self.a ** self.b
    def div(self):
        if self.b == 0:
            return 'err'
        else:
            return self.a / self.b


class test:
    class test1:
        class test2:
            def add(self,a,b):
                return a+b

class tet:
    def add(self,a,b):
        return a+b

# ctrl + /
# from mod import mod1
# a = mod1.add(1,2)
# mod1.fourcal_pickle(1,0).add()
# a = mod1.test.test1.test2()
# print(a.add(1,2))
# b = mod1.tet()
# print(b.add(1,2))