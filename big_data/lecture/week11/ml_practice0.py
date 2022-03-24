import pandas as pd
df = pd.read_csv('/Users/junho/Desktop/main/big_data/lecture/week11/imdb.zip')
df

import tensorflow as tf
token = tf.keras.preprocessing.text.Tokenizer(num_words=2000,oov_token='<unk>')
token.fit_on_texts(df['review'])
token.word_index
token.index_word
token.word_index['good']
token.index_word[31]

import joblib
joblib.dump(token,'tokenizer.pkl')
token = joblib.load('tokenizer.pkl')
token.word_index

token.texts_to_sequences(df['review'])

import tensorflow as tf
tf.keras.losses.SparseCategoricalCrossentropy