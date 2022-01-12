a = {(1,2):'a'} # 키값은 변경 불가능한 값으로 지정가능
del a[1]
a[2] = 'b'
a['name'] = 'pay'
a[3] = [1,2,3]
del a['name']
for k in a.keys():
    print(k)
list(a.keys())
a.values()
a.items()
a.get(2)
a.get('f','bar')
'name' in a
1 in a

for (a,b) in [[1,2],(3,4)]:
    print(a+b)

a = [4,5,6,3]
for x in range(len(a)):
    if a[x]<4:
        continue
    print(a[x])

v = int(input())
for x in range(10):
    print(v*x)