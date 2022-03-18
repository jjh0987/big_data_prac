# TF : term frequency (등장빈도) : 각 단어가 등장한 문장 혹은 문서의 수
# IDF : inverse term frequency (등장빈도 역수) : 총 문서 수 / df
# 중요한 단어이지만 어차피 고르게 퍼져 있는 경우에 이용
# 여러 문서에서 해당 단어가 자주나오면 df 상승 idf 하락
# 각 문서의 특징을 뽑고 싶을때 이용하기 좋은 지표
# 혹은 가중치로 이용하기
import pandas as pd
df = pd.read_excel('/Users/junho/Desktop/main/big_data/lecture/week10/data/imdb.xlsx',index_col=0)
df.head()

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=500,stop_words='english')
tdm = tfidf.fit_transform(df['review'])
tdm

word_count = pd.DataFrame({
    '단어':tfidf.get_feature_names_out(),
    'tf-idf':tdm.sum(axis=0).flat
})
word_count.sort_values('tf-idf',ascending=False).head(5) # tf-idf : tf*idf

dict(zip(tfidf.get_feature_names(),tfidf.idf_))

