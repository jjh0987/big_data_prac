import pandas as pd
import seaborn as sns

# 08-1
tips = sns.load_dataset('tips')
tips.dtypes
tips['sex'] = tips['sex'].astype(str)
tips.dtypes

# category type ?
tips_miss = tips.head(5)
tips_miss
tips_miss.loc[[1,3],'total_bill'] = 'missing'
tips_miss
tips_miss.dtypes # total_bill type : float -> object
# tips_miss['total_bill'] = pd.to_numeric(tips_miss['total_bill'],errors=)
# errors option : raise : 숫자로 변환할 수 없으면 오류발생 default
# coerce : 숫자로 변환할 수 없으면 null
# ignore : 그냥 지나침.
tips_miss['total_bill'] = pd.to_numeric(tips_miss['total_bill'],errors='coerce')
tips_miss
tips_miss.dtypes # 타입이 변경됨

tips_miss['total_bill'] = pd.to_numeric(tips_miss['total_bill'],errors='ignore')
tips_miss
tips_miss.dtypes

# 08-2
# 카테고리 타입 : 동일 문자열이 반복되는 경우 데이터프레임 용량이 줄어든다.
# 용량과 속도의 이점.
# 컬럼의 값들이 몇가지 안되는 경우.
tips

# 09-3
var = 'flesh wound'
s = 'it is just a {}!'
print(s.format(var))
var = 'ha'
s = '{0},{0}'
print(s.format(var))
s = '{max},{min}'
print(s.format(max=1,min=0))
s = '{:,}'
print(s.format(3333))
s = '{0:.4},{0:.4%}'
print(s.format(7/10000))
s = '{0:05d}'
print(s.format(42))

# var = 10
# f 포맷팅 : f'{var}'


# 10-2
import pandas as pd
df = pd.DataFrame({'a':[10,20,30],'b':[20,30,40]})
print(df['a']**2)

def my_sq(x):
    return x**2
def my_exp(x,n):
    return x**n

sq = df['a'].apply(lambda x : my_sq(x))
sq = df['a'].apply(my_sq)
ex = df['a'].apply(lambda x : my_exp(x,2))
ex = df['a'].apply(my_exp,n=3)
ex

def print_me(x):
    print(x)
df.apply(print_me)
df.apply(print_me,axis=0)

def avg(x,y,z):
    return (x+y+z)/3

def avg(col):
    return (col[0]+col[1]+col[2])/3
df.apply(avg)

# default apply : 열방향 연산
def avg(row):
    sum = 0
    for item in row:
        sum += item
    return sum/df.shape[1]

df.apply(avg,axis=1)

# 10-3
import seaborn as sns
import numpy as np
titanic = sns.load_dataset('titanic')
titanic.info()

def count_missing(vec):
    null_vec = pd.isnull(vec)
    return np.sum(null_vec)

titanic.apply(count_missing)

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num/dem

titanic.apply(prop_missing)
titanic['missing'] = titanic.apply(count_missing,axis=1)
row_missing = titanic[titanic['missing'] >= 1]
len(row_missing)
row_missing['missing'].min()