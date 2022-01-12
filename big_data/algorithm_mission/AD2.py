S = input()
target = ['()','[]','{}']
while S != '':
    temp = S
    for i in target:
        S = S.replace(i,'')
    if temp == S:
        break
if len(S) == 0:
    print(True)
else:
    print(False)