# fit interface : y 잘퍈 이용 옵션
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.datasets import load_boston

boston = load_boston()
boston
boston_label = boston.target
bostonDF = pd.DataFrame(data=boston.data,columns=boston.feature_names)
bostonDF['PRICE'] = boston_label

bostonDF.info()
bostonDF.describe()
fig,axs = plt.subplots(figsize=(16,8),ncols=4,nrows=2)
fig
axs

# too minor..
features = ['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
for i,feature in enumerate(features):
    row = int(i/4)
    col = i%4
    sns.regplot(x=feature,y='PRICE',data=bostonDF,ax=axs[row][col])


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

label = bostonDF['PRICE']
X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)

# X_train,X_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.3,random_state=156)

X_train,X_test,y_train,y_test = train_test_split(X_data,label,test_size=0.3,random_state=156)
lr = LinearRegression()
lr.fit(X_train,y_train)

pred = lr.predict(X_test)
mse = mean_squared_error(pred,y_test)
rmse = np.sqrt(mse)
r2_score(pred,y_test)

lr.intercept_ # y 절편
lr.coef_ # 회귀 계수
len(boston.feature_names)

coeff = pd.Series(data=np.round(lr.coef_,2),index=boston.feature_names)
coeff.sort_values(ascending=False)

from sklearn.model_selection import cross_val_score
neg_mse_scores = cross_val_score(lr,X_data,label,scoring='neg_mean_squared_error',cv=5)
rmse_scores = np.sqrt(-1*neg_mse_scores)
avg_rmse = np.mean(rmse_scores)

# mse 작을수록 적합도 높다.(trivial)
neg_mse_scores
rmse_scores
avg_rmse

# L2 regression (ridge)
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=10) # 다음이 성립하는 W 로 수정. Min(RSS(W):squared error + alpha* W:L2 square) # 다중선형에서 가중치 수정
neg_mse_scores = cross_val_score(ridge,X_data,label,scoring='neg_mean_squared_error',cv=5)
rmse = np.sqrt(-1*neg_mse_scores)
avg_rmse = np.mean(rmse_scores)

min(rmse)

alphas = [0,0.1,1,10,100]
for alpha in alphas:
    ridge = Ridge(alpha=alpha)  # Min(RSS(W) + alpha* W:L2 square) # 다중선형에서 가중치 수정 # 회귀 계수 블러링
    neg_mse_scores = cross_val_score(ridge, X_data, label, scoring='neg_mean_squared_error', cv=5)
    rmse = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse_scores)

    print(np.mean(rmse))


coeff_df = pd.DataFrame()
fig,axs = plt.subplots(figsize=(18,6),nrows=1,ncols=5)
for pos,alpha in enumerate(alphas):
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train,y_train)

    coeff = pd.Series(data=ridge.coef_,index=boston.feature_names)
    colname = str(alpha)
    coeff_df[colname] = coeff.sort_values(ascending=False)

    coeff.sort_values(ascending=False,inplace=True)
    sns.barplot(x=coeff.values,y=coeff.index,ax=axs[pos])
# plt.close()

coeff_df


# lasso : alpha* W:L1
# lasso : parm : alpha , equiv to Ridge
# ElasticNet : RSS(W) + alpha1 * W:L1 + alpha2 * W:L2 square
# alpha 인풋은 하나이고, 내부적으로 분할시켜서 이용된다.

from sklearn.linear_model import ElasticNet
EN = ElasticNet(alpha=10,l1_ratio=0.7) # 다음이 성립하는 W 로 수정. Min(RSS(W):squared error + alpha* W:L2 square) # 다중선형에서 가중치 수정
neg_mse_scores = cross_val_score(EN,X_data,label,scoring='neg_mean_squared_error',cv=5)
rmse = np.sqrt(-1*neg_mse_scores)
avg_rmse = np.mean(rmse_scores)

rmse



alphas = [0,0.1,1,10,100]
for alpha in alphas:
    EN = ElasticNet(alpha=alpha,l1_ratio=0.7)  # Min(RSS(W) + alpha* W:L2 square) # 다중선형에서 가중치 수정 # 회귀 계수 블러링
    neg_mse_scores = cross_val_score(EN, X_data, label, scoring='neg_mean_squared_error', cv=5)
    rmse = np.sqrt(-1 * neg_mse_scores)
    avg_rmse = np.mean(rmse_scores)

    print(np.mean(rmse))

coeff_df = pd.DataFrame()
# fig,axs = plt.subplots(figsize=(18,6),nrows=1,ncols=5)
for pos,alpha in enumerate(alphas):
    EN = ElasticNet(alpha=alpha)
    EN.fit(X_train,y_train)

    coeff = pd.Series(data=EN.coef_,index=boston.feature_names)
    colname = str(alpha)
    coeff_df[colname] = coeff.sort_values(ascending=False)

    coeff.sort_values(ascending=False,inplace=True)
    # sns.barplot(x=coeff.values,y=coeff.index,ax=axs[pos])

coeff_df