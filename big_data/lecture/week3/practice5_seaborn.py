import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
type(titanic) # pandas dataFrame
titanic.head()
titanic.info()

# thema : darkgrid,whitegrid,dark,white,ticks
# sns.set_style('dark')
# scatter with regression line
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='age',y='fare',data=titanic,ax=ax1)
sns.regplot(x='age',y='fare',data=titanic,ax=ax2,color='pink')
plt.show()

# hist and density graph
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
sns.distplot(titanic['fare'],ax=ax1)
sns.distplot(titanic['fare'],hist=False,ax=ax2)
sns.distplot(titanic['fare'],kde=False,ax=ax3)
plt.show()

# heat map
table = titanic.pivot_table(index='sex',columns='class',aggfunc='size')
type(table)
sns.heatmap(table,annot=True,fmt='d',cmap='YlGnBu',linewidth=1,cbar=False)
sns.heatmap(data=table,annot=True,fmt='d',cmap='YlGnBu',linewidth=1,cbar=False)
# data : rectangular dataset -> DataFrame
# annot : 구역내 빈도
# fmt : data format
# cbar : color bar
plt.show()

# scatter
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.stripplot(x='class',y='age',data=titanic,ax=ax1)
sns.swarmplot(x='class',y='age',data=titanic,ax=ax2)
# swarmplot : 밀도를 어느정도 표시해준다.

# bar graph
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
sns.barplot(x='sex',y='survived',data=titanic,ax=ax1)
sns.barplot(x='sex',y='survived',hue='class',data=titanic,ax=ax2)
sns.barplot(x='sex',y='survived',hue='class',dodge=False,data=titanic,ax=ax3)
ax1.set_title('titanic survived-sex')
ax2.set_title('titanic survived-sex/class')
ax3.set_title('titanic survived-sex/class stacked')
# hue : group by 시켜준다.
# dodge : default=True, False 경우 한 막대에 쌓인다.

# count graph
sns.countplot(x='class',palette='Set2',data=titanic)
sns.countplot(x='class',data=titanic,hue='who')
sns.countplot(x='class',data=titanic,hue='who',dodge=False)
# palette : color group

# prac
sns.boxplot(x='alive',y='age',palette='Set2',data=titanic)
sns.violinplot(x='alive',y='age',hue='sex',palette='Set2',data=titanic)