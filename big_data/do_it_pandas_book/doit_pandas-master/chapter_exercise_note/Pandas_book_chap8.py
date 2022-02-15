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