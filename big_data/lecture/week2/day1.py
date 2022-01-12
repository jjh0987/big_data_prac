import pandas as pd
df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']]
                  ,index=['준서','예은']
                  ,columns=['나이','성별','학교'])
print(df)
print(df.index)
print(df.columns)
df.rename(columns={'연령':'age','성별':'gender','학교':'school'},inplace=True)
# inplace True 경우, df에 바로 적용된다. (return)
print(df)
df.rename(columns={'age':'나이','성별':'gender','학교':'school'},inplace=False)
# inplace False 경우, 변수에 할당하지 않으면 print만 된다.
print(df)
exam_data = {}
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data,index=['서준','우현','인아'])
df2 = df.copy()
df2.drop('우현',axis=0,inplace=True)
df2
df3 = df.copy()
df3.drop(['우현','인아']) # defalt inplace false 확인후 true설정
df3.drop(['우현','인아'],inplace=True) # drop axis : default = 0
df3
df3.drop(['수학'],axis=0)
df3.drop(['수학'],axis=1) # axis=1 : drop column

exam_data = {}
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data,index=['서준','우현','인아'])
label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print(position1)

label2 = df.loc[['서준','우현']]
print(label2)
position2 = df.iloc[[0,1]] # 인덱스 컬럼 위치 고려
print(position2)

label3 = df.loc['서준':'우현']
print(label3)
position3 = df.iloc[0:1]
print(position3)

exam_data = {}
exam_data['이름'] = ['서준','우현','인아']
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data)
print(df)
math1 = df['수학']
print(math1)
type(math1)

eng1 = df.영어
print(eng1)
type(eng1)
type(df)

df.iloc[::2]
df.iloc[0:3:2]
df.iloc[::-1]

exam_data = {}
exam_data['이름'] = ['서준','우현','인아']
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data)
df
df.set_index('이름',inplace=True)
df.loc['서준',['음악']] # index column 순
df.iloc[0,[1]]
df.loc['서준','음악':'체육']
df.iloc[0,2:]
df.iloc[0:2,0:2]
df.iloc[:,:]

exam_data = {}
exam_data['이름'] = ['서준','우현','인아']
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data)
df['국어'] = 80
df
df.loc[3] = 0
df.loc[4] = ['동규',90,80,70,60,50]
df.loc[5] = df.loc[3]
df.iloc[4,1] = 10
df = df.transpose()
df.iloc[3] = 0
df = df.T

df = df.drop([3,5])
df.iloc[3] = 0
df.loc[3] = 0
df
new_idx = [0,1,2,'a','b','c']
df = df.reindex(new_idx) # ,fill_value= 옵션
len(df)
df.iloc[3,0] = 'ㅎㅎ'
df = df.reset_index()
df

df.drop(0,inplace=True)
df
df.loc[0] = 0
df.loc['a'] = 0
df.sort_index() # str 포함시 불가 int 형만 가능
df.drop('a',inplace=True)
df = df.sort_index(ascending=True) # default True
df

exam_data = {}
exam_data['이름'] = ['서준','우현','인아']
exam_data['수학'] = [90,80,70]
exam_data['영어'] = [98,85,95]
exam_data['음악'] = [85,95,100]
exam_data['체육'] = [100,90,90]
df = pd.DataFrame(exam_data)
df
df.sort_values(by='수학') # ascending = True : default
df.sort_values(by='수학',ascending=False)

student = pd.Series({'국어':100,'영어':50})
student/100 # series 는 연산이 가능하다. data frame은 불가능.
student1 = pd.Series({'국어':50,'영어':100})
addition = student1 + student
subtraction = student1 - student
multiplication = student1 * student
division = student1 / student
result = pd.DataFrame([addition,subtraction,multiplication,division]
                      ,index=['add','sub','mul','div'])
result
# 시리즈 연산시, 인덱스 값끼리 매치되어 연산이된다

import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print(type(df))
df
df + 1 # 프린팅만되고, int형만 연산

df.tail()
addition = df + 10
subtraction = addition - df # 데이터 프레임과의 연산
subtraction
titanic.shape
titanic.head()
titanic.info() # 컬럼명,데이터갯수,데이터타입
titanic.describe() # 전체데이터의 기초 통계
titanic.count() # info에 포함된 정보
titanic['sex'].value_counts() # 해당컬럼의 값분포
titanic['fare'].mean() # median,max,min,std,corr -> describe 에 포함된 정보
titanic['fare'].plot