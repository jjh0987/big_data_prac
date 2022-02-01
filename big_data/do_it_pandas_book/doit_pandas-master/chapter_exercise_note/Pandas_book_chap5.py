# 05-2
import pandas as pd
df1 = pd.read_csv("./data/concat_1.csv")
# 주피터에서 상대경로가 되므로 주피터를 이용 (버그인듯 하다..)
# 절대경로 테스트
df1 = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/concat_1.csv")
# df2 = pd.read_csv("./data/concat_2.csv") # ./ 만 작동하지 않는다.
df2 = pd.read_csv('../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/concat_2.csv')
df3 = pd.read_csv('../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/concat_3.csv')
row_concat = pd.concat([df1,df2,df3])
row_concat.iloc[3,:]
new_row0 = pd.Series(['n1','n2','n3','n4'])
new_row0
row_concat0 = pd.concat([df1,new_row0])
row_concat0 # 컬럼 모양으로 추가된다.

new_row1 = pd.DataFrame([['n1','n2','n3','n4']],columns=['A','B','C','D'])
row_concat1 = pd.concat([df1,new_row1])
row_concat1

new_row2 = pd.DataFrame([['n1','n2','n3','n4']])
row_concat2 = pd.concat([df1,new_row2])
row_concat2 # 컬럼 인덱스가 일치하지 않으면 새로운 컬럼의 로우로 지정된다.

new_row3 = pd.DataFrame([['n1'],['n2'],['n3'],['n4']])
row_concat3 = pd.concat([df1,new_row3])
row_concat3 # row_concat0 와 일치한다.

new_row_df = pd.DataFrame([['n1','n2','n3','n4']],columns=['A','B','C','D'])
df1.append(new_row_df)
df1.append(new_row_df,ignore_index=True) # 새로운 df의 로우인덱스를 무시하고 새로정렬.

row_concat = pd.concat([df1,df2,df3],ignore_index=True) # concat 에서도 사용가능 default : false
row_concat

col_concat = pd.concat([df1,df2,df3],axis=1) # default : axis=0
col_concat
col_concat['A'] # 컬럼값이 중복일경우 모두 불러올 수 있다.
col_concat[['A']]
col_concat['A'] = [1,1,1,1]
col_concat0 = pd.concat([df1,df2,df3],ignore_index=True,axis=1)
col_concat0
col_concat0['A'] = [1,2,3,4]

df1.columns = ['A','B','C','D']
df2.columns = ['E','F','G','H']
df3.columns = ['A','C','F','H']
row_concat = pd.concat([df1,df2,df3]) # 컬럼맵핑에서 존재하는 값만 출력
row_concat
print(pd.concat([df1,df2,df3],join='inner'))
print(pd.concat([df1,df3],join='inner'))

df1.index = [0,1,2,3]
df2.index = [4,5,6,7]
df3.index = [0,2,5,7]
col_concat = pd.concat([df1,df2,df3],axis=1)
col_concat
print(pd.concat([df1,df3],axis=1,join='inner')) # defaul : outer

# 05-3
df1 = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/survey_person.csv")
df2 = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/Survey_site.csv")
df3 = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/survey_survey.csv")
df4 = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/survey_visited.csv")
merge0 = df2.merge(df4,left_on='name',right_on='site')
merge0 # union 파트가 있는 컬럼선택