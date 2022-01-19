import csv
import matplotlib.pyplot as plt
import random

size = [2441,2312,1031,1233]
label = ['A','B','AB','O']
color = ['darkmagenta','deeppink','hotpink','pink']

plt.pie(size,labels=label,autopct='%.1f%%',colors=color,explode=(0,0,0.2,0))
plt.axis('equal') # 정확한 원형표시하기 위함
plt.rc('font',family='Malgun Gothic')
plt.legend(label)

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

M = [int(i) for i in temp[:101]]
F = [int(i) for i in temp[103:]]

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.plot(range(101),M,label='M',color='blue')
plt.plot(range(101),F,label='F',color='red')

plt.title(location+' 남녀성별,지역 인구 구조')
plt.legend()
#plt.grid()
#plt.style.use('ggplot')
f.close()


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

M = [int(i) for i in temp[:101]]
F = [int(i) for i in temp[103:]]
diff = []
for i in range(len(M)):
    diff.append(M[i]-F[i])

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.bar(range(101),diff,label='Differce of gender')

plt.title(location+' (남성 수 - 여성 수)의 인구 구조')
plt.legend()
#plt.grid()
#plt.style.use('ggplot')
f.close()

size = [10,20,30]
color = ['red','blue','green']
plt.scatter([1,2,3],[10,30,20],s=size,c=color)
plt.colorbar()

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
M = [int(i) for i in temp[:101]]
F = [int(i) for i in temp[103:]]

plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
plt.scatter(M,F)
plt.plot([0,7000],[0,7000],color='blue')
plt.title(location+' 의 인구 구조')
#plt.grid()
#plt.style.use('ggplot')
f.close()

x=[]
y=[]
size=[]
for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x,y,s=size,c=size,cmap='jet',alpha=0.5) # alpha : 투명도 0~1
plt.colorbar()