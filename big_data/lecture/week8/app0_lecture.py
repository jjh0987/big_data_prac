import numpy as np
import pandas as pd


path = '../main/big_data/lecture/week8/data/StudentsPerformance.csv'
df = pd.read_csv(path)

df['avg'] = df[['math score','reading score','writing score']].mean(axis=1)
score_df = df.loc[:,['math score','reading score','writing score']]

df.info()

score_df.corr() # 상관계수 출력

import seaborn as sns
sns.heatmap(score_df.corr(),annot=True) # annot 구간값 출력
sns.palplot(score_df[['math score','reading score','writing score']]) # ?

sns.catplot(x='lunch',y='math score',hue='gender',kind='boxen',data=df)
sns.catplot(x='lunch',y='reading score',hue='gender',kind='boxen',data=df)
sns.catplot(x='lunch',y='writing score',hue='gender',kind='boxen',data=df)
df.drop(['math score','reading score','writing score'],axis=1,inplace=True)

sns.catplot(x='lunch',y='avg',hue='gender',kind='boxen',data=df)
