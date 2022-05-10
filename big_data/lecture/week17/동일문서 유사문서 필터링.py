import pandas as pd
data = pd.read_csv('/Users/junho/Downloads/네이버금융종목뉴스기사본문_카카오_전체_전처리후_관련기사제거.csv')
data.info()
data = data.drop_duplicates('기사')
data = data.drop_duplicates('제목')
data = data.drop('링크',axis=1)
data = data.reset_index()
data = data.drop('index',axis=1)
data.info()
data = data.dropna() # 1개 기사

from konlpy.tag import Okt
okt = Okt()
# [okt.nouns(i) for i in list(data['기사'])]
from gensim.models import Word2Vec

model = Word2Vec([okt.nouns(i) for i in list(data['기사'])], min_count=4, seed=65)
model.wv.most_similar('카카오')


from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer(max_features=50000,min_df=2)
m = count_vec.fit_transform(data.loc[:,'기사'])
target = m.toarray()

from numpy import dot
from numpy.linalg import norm
import numpy as np
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

mark = []
for idx1 in range(len(target)):
    for idx2 in range(idx1+1,len(target)):
        if cos_sim(target[idx1],target[idx2]) > 0.5:
            mark.append(idx1)
    print(f'check{idx1}')
len(set(mark)) # 0.7:245, 0.6:374, 0.5:690

from sklearn.feature_extraction.text import TfidfVectorizer
tf_vec = TfidfVectorizer(max_features=50000,min_df=2)
m = tf_vec.fit_transform(data.loc[:,'기사'])
target = m.toarray()

from numpy import dot
from numpy.linalg import norm
import numpy as np
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

mark = []
for idx1 in range(len(target)):
    for idx2 in range(idx1+1,len(target)):
        if cos_sim(target[idx1],target[idx2]) > 0.6:
            mark.append(idx1)
    print(f'check{idx1}')
len(set(mark)) # 0.6:298