# n
arr = list(map(int,input().split()))
default = 1
for i in arr:
    default = default*i
ans = []
for i in arr:
    ans.append(int(default/i))
print(ans)