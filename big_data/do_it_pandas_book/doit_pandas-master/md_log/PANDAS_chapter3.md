# PANDAS_chapter3

## 03-1

### 1. Series

```python
import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series(['banana',42])
s = pd.Series(['jjh','creator of pandas'],index=['people','who'])

```

### 2. DataFrame

```python
scientists = pd.DataFrame({ 
    'Name': ['Rosaline Franklin', 'William Gosset'], 
    'Occupation': ['Chemist', 'Statistician'], 
    'Born': ['1920-07-25', '1876-06-13'], 
    'Died': ['1958-04-16', '1937-10-16'], 
    'Age': [37, 61]}) 
print(scientists)
# 로우인덱스가 따로없기때문에 0,1,2 ... 
# dict 형식이 아니여도 가능하다.
```

```python
import pandas as pd
scientists = pd.DataFrame([['a',1]],columns=['name','year'])
print(scientists)
# 중첩리스트로 행열을 고려한다.
#   name  year
# 0    a     1
```

```python
scientists = pd.DataFrame( 
    data={'Occupation': ['Chemist', 'Statistician'], 
          'Born': ['1920-07-25', '1876-06-13'], 
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset']) 
print(scientists)
```

```python
# dict type을 이용해서 DataFrame을 만들때 dictionary 정렬
from collections import OrderedDict
scientists = pd.DataFrame(OrderedDict(
    [('Name',['Frank','William']),
     ('occupation',['chemist','doctor'])
     ]))
print(scientists)
```

## 03-2, 03-3

### 1. Series 데이터 추출

```python
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'],
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'])
first_row = scientists.loc['William Gosset']
print(first_row) # Series
print(first_row.index) # columns
print(first_row.index[0])
print(first_row.keys()) # columns
print(first_row.keys()[0])
print(first_row.values) # row
ages = scientists['Age']
type(ages) # column : Series
print(ages.mean())
print(ages.std())
name = scientists.index
type(name) # index type *
```

---

```python
ages = scientists['Age']
born = scientists['Born']
temp = ages.append(born)
Rosaline Franklin            37
William Gosset               61
Rosaline Franklin    1920-07-25
William Gosset       1876-06-13
dtype: object
type(temp) # Series : 단순히 붙임

dict_data = {}
dict_data['c0'] = [1,1,3]
dict_data['c1'] = [4,5,6]
dict_data['c2'] = [7,8,9]
df = pd.DataFrame(dict_data,index=['r0','r1','r2'])
# series 연산
s1 = df.iloc[0].sort_index(ascending=False)
s2 = df.iloc[1]

s1.add(s2,fill_value=0) # null 처리
s1.mul(s2,fill_value=0)
s1.min()
s1.isin(s2).sort_index() # set operation 처럼 이용가능
s1.sample() # s1 에서 랜덤추출
type(s1.to_frame()) # DF 로 변형
```



### 2. Series boolean 추출, broadcasting

```python
scientists = pd.read_csv(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\scientists.csv')
ages = scientists['Age']
print(ages.max())
print(ages.mean())
print(ages[ages > ages.mean()]) # boolean 추출 **
temp.reset_index()[['Age']]
print(ages > ages.mean())
bool_values = [True,True] 
ages[[x for x in range(3)]] # line 9 와같은 불린도 넣을 수 있다.
ages * ages # 원소별 연산 (broadcasting)
```

---

```python
temp = pd.Series([0,20])
ages + temp
# null 을 연산하면 null return
0    37.0
1    81.0
2     NaN
3     NaN
4     NaN
5     NaN
6     NaN
7     NaN
dtype: float64
```



## 03-4, 03-5

### 1. DataFrame boolean 추출, broadcasting

```python
subdf = scientists[scientists['Age'] > scientists['Age'].mean()]

scientists*2 # 각 데이터 형식에 *2 (broadcasting)
(scientists*2).shape 
scientists.shape
```



### 2. datetime 자료형

```python
born_date = pd.to_datetime(scientists['Born'],format='%Y-%m-%d') # default
scientists # 8x5
died_date = pd.to_datetime(scientists['Died'])
scientists['born_date'],scientists['died_date'] = (born_date,died_date)
scientists['age_data_dt'] = died_date - born_date
scientists # 8x8
```



### 3. drop

```python
scientists.drop(['Age'],axis=1) # 행 삭제
scientists.drop('Age',axis=1)
scientists.drop(1,axis=0) # 열 삭제
```



## 03-6

### 1. Pickle로 저장, 불러오기

```python
names = scientists['Name']
names.to_pickle(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\test.pickle')
df = pd.read_pickle(r'..\big_data\do_it_pandas_book\doit_pandas-master'
                         r'\chapter_exercise_note\data\test.pickle')
# 이외에도 to_csv(<dir>), to_tsv(<dir>) 이용 가능.
# to_frame()
```

