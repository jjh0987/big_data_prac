def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1) # dict 형식으로 리턴

def add_and_mul(a,b):
    return a+b,a*b
add_and_mul(2,3)
re1_add,re2_mul = add_and_mul(2,3)

def say_myself(name,old,man=True):
    print(name)
    print(old)
    if man:
        print('man')
    else:
        print('woman')

say_myself('jjh',30)
say_myself('jjh',30,False)

a = 1
def vartest():
    global a
    a += 1
vartest()
print(a)

add = lambda a,b:a+b
result = add(3,4)
print(result)

f = open('abc.txt', 'w')
f.close()
f = open('abc.txt', 'w')
for i in range(1,11):
    data = '%d 번째\n' %i
    f.write(data)
f.close()
f = open('abc.txt', 'r')
while 1:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open('abc.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('abc.txt', 'r')
data = f.read()
print(data)
f.close()

f = open('abc.txt', 'a')
for i in range(11,20):
    data = '%d 번째\n'%i
    f.write(data)
f.close()

f = open('foo.txt', 'w')
f.write('life is too short')
f.close()

with open('foo.txt', 'w') as f:
    f.write('you need python')

x = {}
x[1] = 'app' # dict로 저장