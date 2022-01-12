list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
li = list1
for i in list2:
    li.append(i)
print(sorted(li))