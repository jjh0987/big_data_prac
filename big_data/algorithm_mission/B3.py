#n^2
T = list(map(int,input().split()))
ans = [0]*len(T)
for i in range(len(T)):
    for j in range(i+1,len(T)):
        if T[i] < T[j]:
            ans[i] += 1
            break
        else:
            if max(T[i:]) == T[i]:
                break
            else:
                ans[i] += 1
print(ans)