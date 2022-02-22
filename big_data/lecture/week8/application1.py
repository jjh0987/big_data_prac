import numpy as np
import pandas as pd

years = [2015,2016,2017,2018,2019]
df_list = []
for year in years:
    path = f'../main/big_data/lecture/week8/data/archive/{year}.csv'
    df_list.append(pd.read_csv(path))

df_list[3].fillna(df_list[3][['Perceptions of corruption']].mean(),inplace=True)
df_list[3].info()

columns_list = []
for df in df_list:
    target = df.columns
    columns_list.append(target)
    print(len(df.columns))
    print(len(df))

columns_list

# idx
# 0 : 'Happiness Score','Economy (GDP per Capita)', 'Family',
#         'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
#         'Generosity'
#       [3,5,6(f),7,8,9,10]

# 1 : 'Happiness Score','Economy (GDP per Capita)', 'Family',
#         'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)',
#         'Generosity'
#       [3,6,7(f),8,9,10,11]

# 2 : 'Happiness.Score','Economy..GDP.per.Capita.', 'Family',
#         'Health..Life.Expectancy.', 'Freedom', 'Generosity',
#         'Trust..Government.Corruption.'
#       [2,5,6(f),7,8,9,10]

# 3 4 : 'Score', 'GDP per capita',
#         'Social support', 'Healthy life expectancy',
#         'Freedom to make life choices', 'Generosity',
#         'Perceptions of corruption'
#       [2,3,4(s),5,6,7,8]

# transform plan
'''
Score,
GDP_per_captia,Life_exp,Freedom,Perceptions of corruption,Generosity
+ family (for 0,1,2), + Social_support (for 3,4)
'''
H_score_list = []
for i in range(len(years)):
    df_target = pd.DataFrame()
    if i < 2:
        df_target['Score'] = df_list[i].iloc[:,3]
    else:
        df_target['Score'] = df_list[i].iloc[:,2]
    H_score_list.append(df_target)

# H_score_list

column = ['GDP_per_captia','Life_exp','Freedom','Perceptions of corruption','Generosity']
df_data_list = []
for i in range(len(years)):
    df_data = pd.DataFrame(columns=column)
    if i < 2: # 0_6:f,1_7:f
        df_data[['GDP_per_captia','Life_exp','Freedom','Perceptions of corruption','Generosity']] = \
        df_list[i][['Economy (GDP per Capita)','Health (Life Expectancy)','Freedom',
                    'Trust (Government Corruption)','Generosity']]
    elif i == 2: # 2_6:f
        df_data[['GDP_per_captia', 'Life_exp', 'Freedom', 'Perceptions of corruption', 'Generosity']] = \
        df_list[i].iloc[:,[5,7,8,9,10]]
    else: # 4:s
        df_data[['GDP_per_captia', 'Life_exp', 'Freedom', 'Perceptions of corruption', 'Generosity']] = \
        df_list[i].iloc[:,[3,5,6,7,8]]

    df_data_list.append(df_data)

df_data_list

from sklearn.model_selection import train_test_split

train_test_bundle = []
for i in range(len(df_list)):
    X_train,X_test,y_train,y_test = train_test_split\
            (df_data_list[i],H_score_list[i],test_size=0.3,random_state=156)
    train_test_bundle.append([X_train,X_test,y_train,y_test])


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import ElasticNet
alphas = [0,0.1,1,10]
rmse_bundle = []
for alpha in alphas:
    temp = []
    for train in train_test_bundle:
        EN = ElasticNet(alpha=alpha,l1_ratio=0.3)  # Min(RSS(W) + alpha* W:L2 square) # 다중선형에서 가중치 수정 # 회귀 계수 블러링
        neg_mse_scores = cross_val_score(EN,train[0],train[2], scoring='neg_mean_squared_error', cv=5)
        rmse = np.sqrt(-1 * neg_mse_scores)
        avg_rmse = np.mean(rmse)
        temp.append(avg_rmse)
    rmse_bundle.append(temp)
    # print(f'Mean of rmse when alpha is {alpha} : ',rmse_bundle)
show_df = pd.DataFrame(data=rmse_bundle,columns=years,index=alphas)
show_df.reindex(alphas)
print('rmse------')
print('alpha')
print(show_df)


coeff_bundle = []
for train in train_test_bundle:

    coeff_df = pd.DataFrame()

    for alpha in alphas:
        EN = ElasticNet(alpha=alpha,l1_ratio=0.3)
        EN.fit(train[0],train[2])

        coeff = pd.Series(data=EN.coef_,index=column)
        colname = 'alpha:'+str(alpha)
        coeff_df[colname] = coeff.sort_values(ascending=False)

        coeff.sort_values(ascending=False,inplace=True)

    coeff_bundle.append(coeff_df)

print('parameter info')
print('test_size=0.3')
print('l1_ratio=0.3')
for i in range(len(coeff_bundle)):
    print()
    print(years[i],'-----'*10)
    print(coeff_bundle[i])