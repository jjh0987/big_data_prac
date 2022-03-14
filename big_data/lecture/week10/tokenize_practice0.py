import gensim
import sklearn
import nltk
import konlpy
# nltk.download()

# 대문자 유지
# 어포스트로피 존재시 분리
from nltk.tokenize import word_tokenize
print(word_tokenize("Don't be fooled")) # punkt error

# 소문자
# 어퍼스트로피 단어포함
from tensorflow.keras.preprocessing.text import text_to_word_sequence
print(text_to_word_sequence("Don't be fooled"))

# 하이픈 유지
# 어포스트로피 존재시 분리
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "don't be foo-led"
print(tokenizer.tokenize(text))

# 문장 토큰화
from nltk.tokenize import sent_tokenize
print(sent_tokenize('sent1. sent2. sent3,sent4.'))
print(sent_tokenize('ph.d. abc.')) # 특정단어는 마침표가 의미가 있으므로 토큰화 되지 않음.

import kss
text = '재밌다.011. 이건111122.ㅎㅎ. 그래?'
print(kss.split_sentences(text))

# 토큰형식 분류
from nltk.tag import pos_tag
text = "I am activity looking for ph.d. students. and you are."
print(pos_tag(word_tokenize(text)))