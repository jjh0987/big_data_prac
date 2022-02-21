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



df_data