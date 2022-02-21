import numpy as np
import pandas as pd


path = '../main/big_data/lecture/week8/data/StudentsPerformance.csv'
df = pd.read_csv(path)
df['avg'] = df[['math score','reading score','writing score']].mean(axis=1)
df.drop(['math score','reading score','writing score'],axis=1,inplace=True)
df.info()

target = df.avg
df.drop(['avg'],axis=1,inplace=True)

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
for alpha in alphas:
    EN = ElasticNet(alpha=alpha,l1_ratio=0.3)  # Min(RSS(W) + alpha* W:L2 square) # 다중선형에서 가중치 수정 # 회귀 계수 블러링
    neg_mse_scores = cross_val_score(EN,labeling_data,target, scoring='neg_mean_squared_error', cv=5)
    rmse = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse)

    print(f'Mean of rmse when alpha is {alpha} : ',np.mean(rmse))

from sklearn.metrics import accuracy_score
coeff_df = pd.DataFrame()
# fig,axs = plt.subplots(figsize=(18,6),nrows=1,ncols=5)
pred_list = []
acc_list = []

for pos,alpha in enumerate(alphas):
    EN = ElasticNet(alpha=alpha,l1_ratio=0.3)
    EN.fit(X_train,y_train)

    coeff = pd.Series(data=EN.coef_,index=df.columns)
    colname = 'alpha:'+str(alpha)
    coeff_df[colname] = coeff.sort_values(ascending=False)

    coeff.sort_values(ascending=False,inplace=True)
    # sns.barplot(x=coeff.values,y=coeff.index,ax=axs[pos])

# 추정이므로 predict 불필요

print('----dummy info')
# decoding
for i in range(len(df.columns)):
    print(encode_list[i],' : ',[j for j in range(len(encode_list[i]))])
print()
print('----ElasticNet weight info')
print(coeff_df)
