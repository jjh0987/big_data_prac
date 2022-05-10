import pandas as pd
data = pd.read_csv('/Users/junho/Downloads/유사기사_제거(유사도기준-0.6).csv')
data.drop('Unnamed: 0',axis=1,inplace=True)
data.value_counts('정보제공')
data.columns

