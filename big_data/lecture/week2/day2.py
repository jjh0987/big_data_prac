import pandas as pd
df = pd.read_excel(r'C:\Users\xcom2\git_bash_practice\big_data\lecture\week2\stocks.xlsx')
df # 절대경로 이용
df = pd.read_excel(r'..\big_data\lecture\week2\stocks.xlsx')
df # 상대경로 이용

dict_data = {}
dict_data['c0'] = [1,1,3]
dict_data['c1'] = [4,5,6]
dict_data['c2'] = [7,8,9]
df = pd.DataFrame(dict_data,index=['r0','r1','r2'])
print(df)
ndf = df.reset_index()
print(ndf)
ndf = df.sort_index(ascending=False)
print(ndf)
ndf = df.sort_values(by='c1',ascending=False)
print(ndf)

s1 = df.iloc[0].sort_index(ascending=False)
s2 = df.iloc[1]
type(s1)
print(s1 + s2) # 인덱스 배치가 달라도 매칭되어 연산된다.
print(s1 + 1)

ndf1 = df.sort_index(ascending=False)
ndf2 = df.sort_index(ascending=True)
ndf1 + ndf2 # 인덱스 배치가 달라도 매칭되어 연산된다.

s1.add(s2,fill_value=0) # null 처리
s1.mul(s2,fill_value=0)
s1.min()
s1.isin(s2).sort_index() # set operation 처럼 이용가능
s1.sample() # s1 에서 랜덤추출
type(s1.to_frame()) # DF 로 변형

df = pd.read_json(r'..\big_data\lecture\week2\read_json_sample.json')
df.index
df.columns
df = pd.read_html(r'..\big_data\lecture\week2\sample.html')
len(df)
df1 = df[0] # 1st table
df1
df2 = df[1].set_index('name') # 2nd table
print(df2)

df = pd.read_csv(r'..\big_data\lecture\week2\auto-mpg.csv')
df.columns = ['mpg','cylinders','displacement','horsepower','weight'
              ,'acceleration','model year','origin','name']
df.head()
df.describe(include='object')
