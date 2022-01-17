# PANDAS_chapter2

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./data/gapminder.tsv',sep='\t')
print(df.head()) # dataframe, head(n=int) option
type(df)
df.shape # tuple
df.columns # object = **str type** or number
df.dtypes # data type of columns
df.info() # df.types + data counts
df.describe() # 기초통계 inclue='all' 컬럼 타입 설정 NaN 은 제외한 정보만 출력된다. all 의 경우 모두 출력.
df['column_name'] # value : int str ...
df[['column_name']] # dataframe
# 호출방식과 dtype
df[one column element] # indexed value 
df['country'][0] # 호출가능
df[list of col name] # DF
df.loc[list,list of col name] # DF
df.iloc[list,list of col index number] # DF
df.loc[element,list] # series
df.loc[list,element] # series
df.loc[element,element] # value : int str ...
df.loc[0,:] # series
df.loc[0,:][0] # value : int object ...
type(df.tail(0)) # DF
type(df.groupby('year')['lifeExp'].mean()) # serise
type(df.groupby('year').mean()) # DF
type(df.groupby('year')) # DFGroupby
type(df.groupby('year')['lifeExp']) #serise groupby
# groupby 후 그룹연산할 수 있는 메써드 이용. sql 형식
df.groupby(['year','continent'])['lifeExp','gdpPercap'].mean()
df.groupby('continent')['country'].nunique() # groupby 후 country의 개수
# ploting
import matplotlib.pyplot as plt
global_yearly_life_exp = df.groupby('year')['lifeExp'].mean()
global_yearly_life_exp.plot()
```

