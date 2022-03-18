# 주제 분석 (본문으로 유추)

import wget
wget.download('https://github.com/euphoris/datasets/raw/master/neurips.zip')
import pandas as pd
df = pd.read_csv('/Users/junho/Desktop/main/neurips.zip')
df.head()
df.columns
df.iloc[0,1] # label
df.iloc[0,2] # data

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = TfidfVectorizer(stop_words='english',max_features=2000)
x = cv.fit_transform(df.abstract) # data_len * features : 축소 행렬
words = cv.get_feature_names()

from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=100,random_state=10)
svd.fit(x)
svd.components_.shape
len(svd.components_[0])