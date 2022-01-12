length = int(input())
text = []
for i in range(length):
    text.append(input())
temp_tx = []
for i in text:
    temp_tx.append(sorted(i))
temp_txt = []
for i in range(length):
    temp = ''
    for j in temp_tx[i]:
        temp += j
    temp_txt.append(temp)
idx = list(set(temp_txt))

ans = []
for i in idx:
    temp = []
    for j in range(length):
        if i == temp_txt[j]:
            temp.append(text[j])
        else:pass
    ans.append(temp)
print(ans)