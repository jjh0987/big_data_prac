arr = list(map(int,input().split()))
arr.append(None)
ans = []
for i in arr:
    if type(i) is int:
        ans.append(i)
    else:
        pass
ans.reverse()
ans.append(None)
print(ans)

# Z2
arr = list(map(int,input().split()))
temp = arr*2
for i in range(0,len(temp),2):
    print(temp[i])

