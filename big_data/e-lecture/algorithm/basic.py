# weapon

X,y = zip(['a',1],['b',2],['c',3])
print(X)
print(y)

seq = [['a',1],['b',2],['c',3]]
print(*seq)
x,y = zip(*seq)
print(x)
print(y)

import numpy as np
np_arr = np.arange(0,16).reshape(4,4)
print(np_arr)

print('a','b',sep='\n')
print(*['a','b'],sep='\n')
print(*[1,2])
print(*[1,2],end='\n')

print(eval('3+5*7'))

arr = [('hong',35),('이순신',75),('아무개',50)]
result = sorted(arr,key=lambda x:x[1],reverse=True) # sorted 후 reverse 기준은 key

from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(dict(counter))
print(counter)

import math
# 최소 공배수 math.lcm 은 3.9 부터 지원
def lcm(a,b):
    return a*b//math.gcd(a,b)

lcm(21,14)

bow = []
bow.insert(1,10) # index,value