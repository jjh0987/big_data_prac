import re
x = input()
text_sp = re.split(':|,',x)

l = []
for i in text_sp:
    l.append(i.lower().split())
text = ''
for i in l:
    for j in i:
        text += j
temp = []
for i in text:
    temp.append(i)
temp_r = list(reversed(temp))
if temp == temp_r:
    print('True')
else:
    print('False')

import re
x = input()
text_sp = re.split(':|,',x)
l = []
for i in text_sp:
    l.append(i.lower().split())
text = ''
for i in l:
    for j in i:
        text += j
temp = []
temp_x = []
for i in text:
    temp.append(i)
    temp_x.append(i)
i = 0
while i < len(text):
    if temp.pop(0) == temp_x.pop(-1):
        i += 1
        if i == len(text):
            print('True')
    else:
        print('False')
        break







x = int(input())
if x%2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

x = 0
for i in range(1,101):
    if i%2 == 1:
        x += i
    else:
        x -= i

x = []
for i in range(3):
    x.append(int(input()))
print(min(x))

x = input().split(',')
temp = 1
for i in range(int(x[1])):
    temp = temp*int(x[0])

x = 0
for i in range(1,101):
    if i%2 == 1:
        x = x - 1/i
    else:
        x = x + 1/i

#o 번문제 체크

l = []
temp = []
for i in range(11):
    l.append(i)
    temp.append(sum(l))

print(sum(temp))

def factorial(x):
    if x > 0:
        y = x*factorial(x-1)
        return y
    else:
        return 1
x = 0
for i in range(1,11):
    x += factorial(i)
print(x)

import numpy as np
x = [int(i) for i in list(10*np.random.rand(100))]
even = 0
odd = 0
for i in x:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print('even:',even,'odd:',odd)

print(factorial(int(input())))

def fibo(x):
    if x > 1:
        ans = fibo(x-1) + fibo(x-2)
        return ans
    elif x == 1:
        return 1
    else:
        return 0
l = []
for i in range(1,21):
    l.append(fibo(i))
print(sum(l))

l = []
for i in range(1,77):
    l.append(i*(78-i))
print(sum(l))

l = []
for i in range(10):
    l.append(int(input()))
print(max(l))

import numpy as np
x = [int(i) for i in list(100*np.random.rand(10))]
rank = sorted(x)
temp_r = list(reversed(rank))
temp = []
for i in x:
    temp.append(temp_r.index(i)+1)

l = []
for i in range(5):
    l.append(int(input()))
even = 0
odd = 0
for i in l:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print('odd:',odd,'even:',even)

n = int(input())
x = 0
for i in range(n+1):
    if i%2 == 0:
        for j in range(i):
            x += j
    else:
        for j in range(i):
            x -= j
print(x)

print(int(input())*9/5+32)

x = input()
l = []
for i in x:
    l.append(i)
rev = []
k = 0
for i in range(len(x)):
    k -= 1
    rev.append(l[k])
print(rev)

x = input()
l = []
for i in x:
    l.append(i)
l.reverse()
print(l)

target = int(input())
l = []
for i in range(target):
    l.append(input())
ans = []
for i in l:
    temp = []
    for j in i:
        temp.append(j)
    ans.append(temp)

n = int(input())
x = 0
for i in range(1,n):
    if i%2 == 0:
        x -= i*(i+1)/2
    else:
        x += i*(i+1)/2
print(x)

l = []
for i in range(1,77):
    l.append(i*(78-i))
print(sum(l))

x = 0
for i in range(1,77):
    x += i*(78-i)
print(x)

from lecture.week1.mod import mod1

a = mod1.add(1, 2)
mod1.fourcal_pickle(1, 0).add()
a = mod1.test.test1.test2()
print(a.add(1,2))
b = mod1.tet()
print(b.add(1,2))
mod1