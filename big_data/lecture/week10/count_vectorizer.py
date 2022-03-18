from konlpy.tag import Okt
import re
okt = Okt()

token = re.sub('(\.)','','정부가 발표하는 물가상승률. 소비자가 느낀 물가상승률')
token = okt.morphs(token)
word_idx = {}
bow = []
for voca in token:
    if voca not in word_idx.keys():
        word_idx[voca] = len(word_idx)
        bow.insert(len(word_idx)-1,1)
        print(word_idx)
    else:
        index = word_idx.get(voca)
        bow[index] = bow[index]+1
print()
print(word_idx)
print(bow)

from sklearn.feature_extraction.text import CountVectorizer
corpus = ['you know I want your love. because I love you']
vector = CountVectorizer()
vector.fit_transform(corpus).toarray() # counter # space 이용한분리
vector.vocabulary_ # dict

vector = CountVectorizer(stop_words=['love','you'])
vector.fit_transform(corpus).toarray()
vector.vocabulary_

vector = CountVectorizer(stop_words='english') # 내장 stopword
vector.fit_transform(corpus).toarray()
vector.vocabulary_

# 외부 stopword 이용
from nltk.corpus import stopwords
stop_word = stopwords.words('english')
vector = CountVectorizer(stop_words=stop_word)
vector.fit_transform(corpus).toarray()
vector.vocabulary_

# 각문장의 count vectorize
from sklearn.feature_extraction.text import CountVectorizer
import wget
import pandas as pd

# 경로 최상단에 로드됨.
wget.download('https://raw.githubusercontent.com/euphoris/datasets/master/imdb.xlsx') # data load
df = pd.read_excel('imdb.xlsx',index_col=0)
df.head(5)
df.shape

c_vec = CountVectorizer(max_features=500,stop_words='english')
term_doc_matrix = c_vec.fit_transform(df['review'])
term_doc_matrix.shape # num of sentence 784, feature 500
c_vec.get_feature_names_out()[:10]

term_doc_matrix.sum(axis=0) # 컬럼 : 단어 , 컬럼의 빈도의 합 (axis 0), axis1 이면 문장길이
term_doc_matrix.sum(axis=1) # axis1 이면 문장길이

import numpy as np
temp = np.array(term_doc_matrix.sum(axis=0)[0]).squeeze()
word_count = pd.DataFrame({'단어':c_vec.get_feature_names_out(),'빈도':temp})
word_count = pd.DataFrame({'단어':c_vec.get_feature_names_out(),'빈도':term_doc_matrix.sum(axis=0).flat})

# 경로 최상단에 저장
# word_count.to_csv('/Users/junho/Desktop/main/big_data/lecture/week10/data/word_count.csv')

from wordcloud import WordCloud
wc = WordCloud(background_color='white',max_words=100,width=400,height=300)
count_dict = word_count.set_index('단어')['빈도'].to_dict()
count_dict = dict(zip(word_count['단어'],word_count['빈도'])) # same
cloud = wc.fit_words(count_dict)
# cloud.to_image()
import matplotlib.pyplot as plt
plt.imshow(cloud)

# cloud.to_file('/Users/junho/Desktop/main/big_data/lecture/week10/data/cloud.png')
import os
os.getcwd() # 최상위 루트