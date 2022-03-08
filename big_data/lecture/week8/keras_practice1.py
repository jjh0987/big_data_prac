import numpy as np
import tensorflow as tf
import pandas as pd

np.random.seed(3)
tf.random.set_seed(3)
path = '../main/big_data/lecture/week8/data/sonar.csv'
df = pd.read_csv(path,header=None)
df.info()

trains_set = df.iloc[:,:60]
encode_target = pd.DataFrame(df.iloc[:,60])

from sklearn import preprocessing
def encoder(df):
    encode_list = []
    features = df.columns
    encode = preprocessing.LabelEncoder()
    for feature in features:
        encode.fit(df[feature])
        df[feature] = encode.transform(df[feature])
        encode_list.append(encode.classes_)
    return df,encode_list

label,encode_list = encoder(encode_target)


from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score


skf = StratifiedKFold(n_splits=5)
for train_index,test_index in skf.split(trains_set,label):
    x_train,x_test = trains_set.iloc[train_index],trains_set.iloc[test_index]
    y_train,y_test = label.iloc[train_index],label.iloc[test_index]

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
initializer = tf.keras.initializers.HeNormal()

model.add(Dense(10,activation='sigmoid',kernel_initializer=initializer))

model.add(Dense(15,activation='relu'))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(5,activation='sigmoid'))

model.add(Dense(1,activation='sigmoid'))

opt = tf.keras.optimizers.Adam(lr=0.1)
model.compile(loss='binary_crossentropy',optimizer=opt,metrics='accuracy')
model.fit(x_train,y_train,epochs=50,batch_size=20)
model.evaluate(x_test,y_test)
# model.predict(test_set)
# -> 후처리 라벨링



# # # # # # #
from tensorflow.keras.datasets import imdb
(train_data,train_label),(test_data,test_label) = imdb.load_data(num_words=10000)
train_data
movie_df = pd.DataFrame()
movie_df['train_data'] = train_data
movie_df['train_labels'] = train_label
# max_val = [max(sequence) for sequence in train_data]
word_idx = imdb.get_word_index()

dict = {i:j for i,j in zip(word_idx.values(),word_idx.keys())}
dict = sorted(dict.items())

' '.join([dict[i] for i in movie_df.loc[0,'train_data']])

# 0 1 2 : 예약 인덱스 : 임시값, 문서시작, 사전에 없음. encoding 시 규칙
# train_data : index 를 3칸 밀어둔 데이터 , -> -3 해주어야 정확한 문장 출력
decode_review = ' '.join([dict.get(i-3,'?') for i in movie_df.loc[0,'train_data']])

# 10000을 인덱스로 치환
def vetorize_seq(seqs,dim=10000):
    results = np.zeros((len(seqs),dim))
    for i,seq in enumerate(seqs):
        results[i,seq] += 1
        print()
    return results
x_train = vetorize_seq(train_data).astype('float32')
x_test = vetorize_seq(test_data).astype('float32')

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
model = models.Sequential()
model.add(layers.Dense(16,activation='relu'))
model.add(layers.Dense(16,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

opt = optimizers.RMSprop(learning_rate=0.001)
loss = losses.binary_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])

model.fit(x_train,train_label,epochs=30,batch_size=100)


x_val = x_train.astype(float)
partial_x_train = x_val[10000:].astype(float)
y_val = train_label
partial_y_train = y_val[10000:].astype(float)
history = model.fit(partial_x_train,partial_y_train,
                    epochs=20,batch_size=100,validation_data=(x_val,y_val))

loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

ephoc = range(1,len(acc)+1)

import matplotlib.pyplot as plt
plt.plot(ephoc,loss,'bo')
plt.plot(ephoc,val_loss,'b')
plt.plot(ephoc,acc,'bo')
plt.plot(ephoc,val_acc,'b')


pred = model.predict(x_test)


'''
from tensorflow.keras.preprocessing.sequence import pad_sequences
vocab_size = 10000
max_len = 500

x_train = pad_sequences(train_data,maxlen=max_len)
x_test = pad_sequences(train_data,maxlen=max_len)

# 빈도수 순위
word_idx = imdb.get_word_index()
word_idx.items()
index_to_word = {}
for key, value in word_idx.items():
    index_to_word[value+3] = key
for index, token in enumerate(("<pad>", "<sos>", "<unk>")):
    index_to_word[index] = token

print(' '.join([index_to_word[index] for index in train_data[0]]))


from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import GRU
model = Sequential()

model.add(Embedding(vocab_size,100))
# model.add(GRU(128))
model.add(Dense(1,activation='sigmoid'))

opt = tf.keras.optimizers.Adam(lr=0.01)
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics='accuracy')
model.fit(x_train,train_label,epochs=50,batch_size=100,validation_split=0.2)

# model.save('')
x_train.shape
train_label.shape
'''