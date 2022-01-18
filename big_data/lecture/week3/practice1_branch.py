import csv
import pandas as pd
import matplotlib.pyplot as plt
f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
# encoding='cp949' : default
data = csv.reader(f)
header = next(data)
# 'r' is default
fill_null = []
for row in data:
    if row[-1] == '':
        row[-1] = 30
        row[-2] = 25
    else:
        row[-1] = float(row[-1])
        row[-2] = float(row[-2])

    fill_null.append(row)

f.close()
temp = []
for i in fill_null:
    temp.append(i[-1])

target = max(temp)
cnt = 0
date = ''
while 1:
    if temp[cnt] == target:
        date += fill_null[cnt][0]
        break
    else:
        cnt += 1
print(fill_null[cnt])
#plt.plot([1,2,3],[1,2,3],color='r',ls='-',label='asc')
#plt.title('x=y')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()

MIN_L = []
MAX_L = []
i = 0
while i < len(fill_null):
    if fill_null[i][0].split('-')[1] == '08' and fill_null[i][0].split('-')[2] == '04':
        MIN_L.append(fill_null[i][-2])
        MAX_L.append(fill_null[i][-1])
    i += 1

fig, ax = plt.subplots()
ax.plot(MIN_L,label='MIN')
ax.plot(MAX_L,label='MAX')
plt.legend()
plt.title('birth_temp')