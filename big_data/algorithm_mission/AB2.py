M,N = map(int,input().split())
listIP = list(map(int,input().split()))
target = list(reversed(listIP[M-1:N]))
temp = []
for i in listIP[:M-1]:
    temp.append(i)
for i in target:
    temp.append(i)
for i in listIP[N:]:
    temp.append(i)
print(temp)