# 06
from numpy import NaN,NAN,nan # 정해지지 않은값.
import pandas as pd
print(NaN == True)
print(NAN == False)
print(nan == 0)
print(NaN == '')
print(pd.isnull(nan)) # True
print(pd.notnull(nan)) # False
print(pd.notnull(42))

visited = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/survey_visited.csv")
survey = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/survey_survey.csv")
vs = visited.merge(survey,left_on='ident',right_on='taken')
vs
gapminder = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/gapminder.tsv",sep='\t')
gapminder.head()
life_exp = gapminder.groupby('year')['lifeExp'].mean()
life_exp
life_exp.loc[range(2000,2010),]
life_exp[life_exp.index > 2000]
type(life_exp)
life_exp.index
gapminder['year'].columns # series has no column
life_exp[2002]

ebola = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/country_timeseries.csv")
ebola.count()
ebola.info
ebola.shape
cnt = 0
for i in ebola['Cases_Guinea'].isnull():
    if i == True:
        cnt += 1
print(cnt)
ebola.Cases_Guinea.value_counts(dropna=False).head()
ebola.fillna(0) # 지정값으로 널값처리
ebola.fillna(method='ffill').iloc[0:10,0:5] # 이전의 값으로 널 채우기
ebola.interpolate().iloc[0:10,0:5] # 널의 양값의 평균 이용
ebola.shape
ebola.dropna() # 널값이 존재하면 삭제.

ebola['Cases_multiple'] = ebola['Cases_Guinea']+ebola['Cases_Liberia']+ebola['Cases_SierraLeone']
ebola['Cases_multiple'] # null 연산 -> null
ebola.Cases_Guinea.sum(skipna=True)
ebola.Cases_Guinea.sum(skipna=False)