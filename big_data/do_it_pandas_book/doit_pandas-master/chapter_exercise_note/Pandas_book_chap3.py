# 03-2
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict

s = pd.Series(['banana',42])
print(type(s))
print(s[0])
print(s)

s = pd.Series(['jjh','creator of pandas'],index=['people','who'])
print(s)
print(s['people'])

scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]})
print(scientists)

scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'])
print(scientists)

scientists = pd.DataFrame([['a',1]],columns=['name','year'])
print(scientists)

scientists = pd.DataFrame(OrderedDict(
    [('Name',['Frank','William']),
     ('occupation',['chemist','doctor'])
     ]))
print(scientists)

scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'])
first_row = scientists.loc['William Gosset']
print(first_row)
print(first_row.index)
print(first_row.index[0])
print(first_row.keys())
print(first_row.keys()[0])
print(first_row.values)
ages = scientists['Age']
type(ages) # column : Series
print(ages.mean())
print(ages.std())
name = scientists.index
type(name)
born = scientists['Born']
temp = ages.append(born)
type(temp)
ages.describe() # Series
scientists.describe() # DF
scientists._get_value('William Gosset','Age')
scientists.values
ages.equals([37,61])

# 03-3
scientists = pd.read_csv(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\scientists.csv')
ages = scientists['Age'] # series
print(ages.max())
print(ages.mean())
temp = ages[ages > ages.mean()] # boolean 추출
temp.reset_index()[['Age']]
print(ages > ages.mean())
bool_values = [True,True]
ages[[x for x in range(3)]]
ages * ages

temp = pd.Series([0,20])
ages + temp

# 03-4
subdf = scientists[scientists['Age'] > scientists['Age'].mean()]
subdf
scientists*2 # 각 데이터 형식에 *2 (broadcasting)
(scientists*2).shape
scientists.shape

# 03-5
born_date = pd.to_datetime(scientists['Born'],format='%Y-%m-%d') # default
born_date
died_date = pd.to_datetime(scientists['Died'])
died_date
scientists['born_date'],scientists['died_date'] = (born_date,died_date)
scientists['age_data_dt'] = died_date - born_date
sdf = scientists['Age']
scientists.drop('Name',axis=1)

# 03-6
names = scientists['Name']
names.to_pickle(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\test.pickle')
df = pd.read_pickle(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\test.pickle')
df
type(df.to_frame())