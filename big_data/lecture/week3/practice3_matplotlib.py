import csv
import matplotlib.pyplot as plt

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

plt.bar(range(10),range(10))

f = open(r'..\big_data\lecture\week3\data\age-gender.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
location = input()
for row in data:
    if location in row[0]:
        target = row[3:]
        break
M = [int(i) for i in target[:101]]
F = [-int(i) for i in target[103:]]

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.barh(range(101),M,label='남성')
plt.barh(range(101),F,label='여성')
#plt.barh() # 그래프 transpose
#plt.plot(age_int)
plt.title(location+' 남녀성별,지역 인구 구조')
plt.legend()
#plt.grid()
#plt.style.use('ggplot')
f.close()
