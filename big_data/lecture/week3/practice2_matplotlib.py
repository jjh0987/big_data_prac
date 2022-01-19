import matplotlib.pyplot as plt
import csv
import random

freq = 10000
bins = 6
dice = []
for i in range(freq):
    dice.append(random.randint(1,6))
print(dice)
plt.hist(dice,bins=bins) # bin : peace of x label
plt.show()

f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
result = []
for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))
plt.hist(result,bins=10)
f.close()

f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
result_12 = []
result_01 = []
for row in data:
    if row[-1] != '':
        if str(row[0].split('-')[1]) == '12':
            result_12.append(float(row[-1]))
        else:
            result_01.append(float(row[-1]))
print(result_12)
print(result_01)
plt.hist(result_12,bins=10)
f.close()

result = []
for i in range(10):
    result.append(random.randint(1,1000))
result.sort()
plt.boxplot(result)

f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
result = []
for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))
plt.boxplot(result)
f.close()

f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
result_12 = []
result_01 = []
for row in data:
    if row[-1] != '':
        if str(row[0].split('-')[1]) == '12':
            result_12.append(float(row[-1]))
        else:
            result_01.append(float(row[-1]))
#print(result_12)
#print(result_01)
#plt.boxplot(result_12)
#plt.boxplot(result_01)
plt.boxplot([result_12,result_01])
f.close()


f = open(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)

# starting data
len_year = 2
temp_year = '2021'
temp_month = '12'
year = []
for i in range(len_year):
    month = [[], [], [], [], [], [], [], [], [], [], [], []]
    for row in data:
        if row[0].split('-')[1] != temp_month:
            temp_month = row[0].split('-')[1]
        elif row[-1] != '':
            month[int(row[0].split('-')[1])-1].append(float(row[-1]))
        if row[0].split('-')[0] != temp_year:
            temp_year = row[0].split('-')[0]
            break
    year.append(month)

conti = []
for i in range(len_year):
    for j in year[i]:
        conti.append(j)

plt.boxplot(conti)
f.close()