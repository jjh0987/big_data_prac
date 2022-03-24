import wget
wget.download('https://github.com/euphoris/datasets/raw/master/neurips.zip')

import pandas as pd
df = pd.read_csv('/Users/junho/Desktop/main/neurips.zip')
df.head() # year title abstract

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = TfidfVectorizer(stop_words='english',max_features=2000)
x = cv.fit_transform(df.abstract)
words = cv.get_feature_names()

from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=100,random_state=10)
x.shape
svd.fit(x) # 3920:data len, 2000:word vec
svd.components_.shape # 100,2000 # 문서를 100으로 축소
svd.components_
word_idx = words.index('topic')
words

svd.components_[:,word_idx]

from matplotlib import pyplot as plt
plt.plot(svd.components_[:,word_idx])
topic_idx = svd.components_[:,word_idx].argmax() # 특정 단어에서 값이 특정 문서에서 가장큰 인덱스
topic_idx

topic = pd.DataFrame({'word':words,'loading':svd.components_[topic_idx]})
topic.sort_values('loading')

# svd value? 값이 클수록 해당단어가 해당 문서에서 가장 영향이 높은 값 # 상관관계와 유사

from factor_analyzer.rotator import Rotator # 높은값만 추출하기 위함.
rotator = Rotator()
rot = rotator.fit_transform(svd.components_.T)
rot.shape
loading = rot.T
word_idx = words.index('topic')
plt.plot(loading[:,word_idx])
loading

topic_idx = loading[:,word_idx].argmax() # word 에서 가장 높은 로우
topic = pd.DataFrame({'word':words,'loading':loading[topic_idx]}) # 해당로우 전체값
topic.sort_values('loading',ascending=False).head()

doc_topics = svd.transform(x)
doc_topics = doc_topics @ rotator.rotation_
doc_topics.shape # 차원축소된 문서들

doc_topics[:,topic_idx]
year_topic = pd.DataFrame({'year':df.year,'topic':doc_topics[:,topic_idx]})
year_topic

year_topic.groupby('year').agg('mean')