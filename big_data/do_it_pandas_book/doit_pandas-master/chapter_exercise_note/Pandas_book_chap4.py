import seaborn as sns
import matplotlib.pyplot as plt

#04-1
anscombe = sns.load_dataset('anscombe')
print(anscombe)
dataset_1 = anscombe[anscombe['dataset']=='I']
plt.plot(dataset_1['x'],dataset_1['y'])
plt.plot(dataset_1['x'],dataset_1['y'],'o')

dataset_2 = anscombe[anscombe['dataset']=='II']
dataset_3 = anscombe[anscombe['dataset']=='III']
dataset_4 = anscombe[anscombe['dataset']=='IV']
# group by 데이터에 대한 row를 모두 가져온다.

plt.figure()
g1 = plt.subplot(2,2,1)
g2 = plt.subplot(2,2,2)
g3 = plt.subplot(2,2,3)
g4 = plt.subplot(2,2,4)
g1.plot(dataset_1['x'],dataset_1['y'],'o')
g2.plot(dataset_2['x'],dataset_2['y'],'o')
g3.plot(dataset_3['x'],dataset_3['y'],'o')
g4.plot(dataset_4['x'],dataset_4['y'],'o')
g1.set_title('data1')
g2.set_title('data2')
g3.set_title('data3')
g4.set_title('data4')
plt.suptitle('anscombe')
plt.tight_layout() # 겹치는 현상 해소

#04-2
tips = sns.load_dataset('tips')
tips
plt.hist(tips['total_bill'],bins=10)
plt.plot(tips['total_bill'],tips['tip'],'o')
plt.plot('total_bill','tip','o',data=tips)
plt.scatter(tips['total_bill'],tips['tip'])
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.title('scatter')
plt.boxplot([tips[tips['sex']=='Male']['tip'],tips[tips['sex']=='Female']['tip']],labels=['Male','Female'])
Male_row = tips[tips['sex']=='Male']
Female_row = tips[tips['sex']=='Female']
type(Male_row)
plt.scatter(Male_row['total_bill'],Male_row['tip'],s=Male_row['size']*10,color='blue')
plt.scatter(Female_row['total_bill'],Female_row['tip'],s=Female_row['size']*10,color='red')

#04-3
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False)
sns.distplot(tips['total_bill'],hist=False)
sns.distplot(tips['total_bill'],rug=True)
sns.countplot('day',data=tips)
sns.regplot(tips['total_bill'],tips['tip'])
sns.regplot(x='total_bill',y='tip',data=tips,fit_reg=False)
sns.jointplot(x='total_bill',y='tip',data=tips)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
sns.kdeplot(data=tips['total_bill'],data2=tips['tip'],shade=True)
sns.barplot(x='time',y='total_bill',data=tips)
sns.boxplot(x='time',y='total_bill',data=tips)
sns.violinplot(x='time',y='total_bill',data=tips)
sns.violinplot(x='time',y='total_bill',data=tips,hue='sex',split=True)
# default of split : False -> hue로 분할된 두개의 바이올린 그래프가 나온다. True 설정 시, 반반씩 출력
# hue : data 분할. violin 의 경우 두개로 나눌 수 있다.
sns.lmplot(x='x',y='y',data=anscombe,fit_reg=True,col='dataset',col_wrap=2) # col= 옵션으로 group by data를 얻을 수 있다.
# row option 도 걸 수 있음
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='smoker')

#04-4
tips['total_bill'].plot.hist() # sns 내장
tips[['total_bill','tip']].plot.hist(bins=20,alpha=0.5) # alpha : 투명도
tips['tip'].plot.kde()
tips.plot.scatter(x='total_bill',y='tip')
tips.plot.hexbin(x='total_bill',y='tip',gridsize=10)
tips.plot.box()