import numpy as np
import pandas as pd


path = '../main/big_data/lecture/week8/data/StudentsPerformance.csv'
df = pd.read_csv(path)
df['avg'] = df[['math score','reading score','writing score']].mean(axis=1)
score_df = df.loc[:,['math score','reading score','writing score']]
df.drop(['math score','reading score','writing score'],axis=1,inplace=True)
df.info()

target = df.avg
df.drop(['avg'],axis=1,inplace=True)

score_df.corr()

import seaborn as sns
sns.heatmap(score_df.corr(),annot=True) # annot 구간값 출력
# sns.palplot(score_df[['math score','reading score','writing score']]) # ?

sns.catplot(x='lunch',y='math score',hue='gender',kind='boxen',data=df)
sns.catplot(x='lunch',y='reading score',hue='gender',kind='boxen',data=df)
sns.catplot(x='lunch',y='writing score',hue='gender',kind='boxen',data=df)
df.drop(['math score','reading score','writing score'],axis=1,inplace=True)

sns.catplot(x='lunch',y='avg',hue='gender',kind='boxen',data=df)

from sklearn import preprocessing
def encoder(df):
    encode_list = []
    features = df.columns
    encode = preprocessing.LabelEncoder()
    for feature in features:
        encode.fit(df[feature])
        df[feature] = encode.transform(df[feature])
        encode_list.append(encode.classes_)
    return df,encode_list

labeling_data,encode_list = encoder(df)
encode_list


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(labeling_data,target,test_size=0.3,random_state=156)


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import ElasticNet
alphas = [0,0.1,1,10]
l1_ratio = 0.3
cv = 5
for alpha in alphas:
    EN = ElasticNet(alpha=alpha,l1_ratio=l1_ratio)
    neg_mse_scores = cross_val_score(EN,labeling_data,target, scoring='neg_mean_squared_error', cv=cv)
    rmse = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse)

    print(f'Mean of rmse when alpha is {alpha} : ',np.mean(rmse))

coeff_df = pd.DataFrame()

for alpha in alphas:
    EN = ElasticNet(alpha=alpha,l1_ratio=l1_ratio)
    EN.fit(X_train,y_train)

    coeff = pd.Series(data=EN.coef_,index=df.columns)
    colname = 'alpha:'+str(alpha)
    coeff_df[colname] = coeff.sort_values(ascending=False)

    coeff.sort_values(ascending=False,inplace=True)


print('----corr of score')
print(score_df.corr())
print()
print('----dummy info')
# decoding
for i in range(len(df.columns)):
    print(encode_list[i],' : ',[j for j in range(len(encode_list[i]))])
print()
print(f'l1 ratio : {l1_ratio}, cv : {cv}')
print('----ElasticNet weight info')
print(coeff_df)
