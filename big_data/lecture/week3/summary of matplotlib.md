# Summary of matplotlib

## 1. 데이터 불러오기

```python
import csv

f = open(r'..\big_data\lecture\week3\data\age.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
for row in data:
    print(row) # 데이터 가공 스텝
f.close()
```



## 2. plt.plot() basic form

```python
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
```



## 3. plot.hist() basic form

```python
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
```



## 4. plot.boxplot() basic form

```python
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
```



## 5. plot.bar() basic form

```python
f = open(r'..\big_data\lecture\week3\data\age.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
location = input()
for row in data:
    if location in row[0]:
        target = row[3:]
        break
age_int = [int(i) for i in target]
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.barh(range(101),age_int)
#plt.barh() # 그래프 transpose
#plt.plot(age_int)
plt.title(location+' 지역 인구 구조')
#plt.grid()
#plt.style.use('ggplot')
f.close()
```



## 6. plot.pie() basic form

```python
f = open(r'..\big_data\lecture\week3\data\age-gender.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
#location = input()
location = '제주특별자치도'
for row in data:
    if location in row[0]:
        target = row[3:]
        break
temp = []
for i in target:
    temp.append(i.replace(',',''))

M = sum([int(i) for i in temp[:101]])
F = sum([int(i) for i in temp[103:]])
label = ['M','F']

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.pie([M,F],labels=label,autopct='%.1f%%',startangle=90,explode=(0,0.01))

plt.title(location+' 남녀성별,지역 인구 구조')
plt.axis('equal') # 정확한 원형표시하기 위함
plt.legend()
#plt.grid()
#plt.style.use('ggplot')
f.close()
```