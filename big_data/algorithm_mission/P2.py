arr = sorted(list(map(int,input().split())))
ans = []
for i in range(0,len(arr),2):
    temp = [arr[i],arr[i+1]]
    ans.append(temp)
summation = 0
for i in ans:
    summation += min(i)
print(summation)