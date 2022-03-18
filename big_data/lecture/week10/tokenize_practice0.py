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

from nltk.stem import WordNetLemmatizer
engine = WordNetLemmatizer()
print(engine.lemmatize('cats')) # stem : cat , affix : s
engine.lemmatize('dies','v')
engine.lemmatize('has','v')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
sentence = 'this was not the map we found in Billy'
tokenized_sentence = word_tokenize(sentence)
tokenized_sentence

print([stemmer.stem(word) for word in tokenized_sentence])

words = ['formalize','allowance','electricical']
print([stemmer.stem(word) for word in words])


from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter_stem = PorterStemmer()
lancaster_stem = LancasterStemmer()
words = ['policy','doing','organization','am','the going','having','has']
print([porter_stem.stem(i) for i in words])
print([lancaster_stem.stem(i) for i in words])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
example = 'family is not an important thing. It"s everything'
word_token = stopwords.words('english')
word_token[:10]

okt = Okt()
example = '고기를 아무렇게나 구우려고 하면 안 돼.'
stopwords = '아무렇게나 안'
stopword = stopwords.split()
word_token = okt.morphs(example)
result = [word for word in word_token if not word in stopword]
print(result)

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
raw_text = 'a barber is a person. a barber is good.'
vocab = {}
sentences = sent_tokenize(raw_text)
preprocessed_sentence = []
stop_words = set(stopwords.words('english'))
for sentence in sentences:
    tokenized_sentence = word_tokenize(sentence)
    result = []
    for word in tokenized_sentence:
        word = word.lower()
        if word not in stopword:
            if len(word) > 2:
                result.append(word)
                if word not in vocab:
                    vocab[word] = 0
                vocab[word] += 1
    preprocessed_sentence.append(result)
print(preprocessed_sentence)
vocab

text = '나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야'
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
print(tokenizer.word_index) # 내부 word_index
print(tokenizer.word_counts)
print(tokenizer.texts_to_sequences([text]))
encode = tokenizer.texts_to_sequences([text])
print(to_categorical(encode)) # setences -> sentence -> word