from tensorflow.keras.datasets import reuters
import pandas as pd
import numpy as np
(train_data,train_label),(test_data,test_label) = reuters.load_data(num_words=10000)
data_df = pd.DataFrame()
data_df['data'] = train_data
data_df['label'] = train_label
data_df.info()

word_idx = reuters.get_word_index()
idx_word = {i:j for i,j in zip(word_idx.values(),word_idx.keys())}
def vetorize_seq(seqs,dim=10000):
    results = np.zeros((len(seqs),dim))
    for i,seq in enumerate(seqs):
        results[i,seq] += 1
        print()
    return results

x_train = vetorize_seq(train_data).astype('float32')
x_test = vetorize_seq(test_data).astype('float32')

# decode_review = ' '.join([dict.get(i-3,'?') for i in data_df.loc[0,'data']])
# decode_review
label_con = len(set(train_label)) # 46
# len(set(test_label)) : 46

from sklearn.metrics import accuracy_score
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = models.Sequential()
model.add(layers.Dense(500,activation='sigmoid'))
model.add(layers.Dense(200,activation='relu'))
model.add(layers.Dense(label_con,activation='softmax'))

opt = optimizers.Adam(learning_rate=0.001)
loss = losses.sparse_categorical_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])



model.fit(x_train,train_label,epochs=10,batch_size=100)
pred = model.predict(x_test)

# print(model.evaluate(x_test,test_label))
one_hot_pred = np.array([np.argmax(i) for i in pred])
acc = accuracy_score(one_hot_pred,test_label)
print(round(acc,4))



#####################
'''
def to_one_hot(labels,dimention=46):
    results = np.zeros((len(labels),dimention))
    for i,label in enumerate(labels):
        results[i,label] = 1
    return results

one_hot_train_labels = to_one_hot(train_label)
one_hot_test_labels = to_one_hot(test_label)
'''
# one hot 한 경우 -> categoricl
# one hot 하지 않은 경우 -> spares_categorical
# model.predict 시 원핫 레이블 출력
idx = 6000
x_val = x_train[:idx]
partial_x_train = x_train[idx:]

y_val = train_label[:idx]
partial_y_train = train_label[idx:]

model = models.Sequential()
model.add(layers.Dense(500,activation='sigmoid'))
model.add(layers.Dense(200,activation='relu'))
model.add(layers.Dense(label_con,activation='softmax'))

opt = optimizers.Adam(learning_rate=0.001)
loss = losses.sparse_categorical_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
history = model.fit(partial_x_train,partial_y_train,
                    epochs=15,batch_size=100,validation_data=(x_val,y_val))

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

print(val_acc[-1])
