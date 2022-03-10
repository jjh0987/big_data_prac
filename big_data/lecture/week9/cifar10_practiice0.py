import numpy as np
import pandas as pd
import os
from tensorflow.keras.datasets import cifar10

(train_images,train_labels),(test_images,test_labels) = cifar10.load_data()
print(train_images.shape,train_labels.shape) # 50000,32,32,3 : rgb type , 50000,1
print(test_images.shape,test_labels.shape)
# label 차원 축소
train_labels = train_labels.squeeze()
test_labels = test_labels.squeeze()
train_labels.shape


names = np.array(['airplane','automobile','bird','cat','dear','dogs',
                  'frog','horse','ship','truck'])

import matplotlib.pyplot as plt
import cv2

plt.imshow(cv2.cvtColor(train_images[0],cv2.COLOR_BGR2RGB))
plt.title(train_labels[0])

def show_images(images,labels,ncols=8):
    figure, axs = plt.subplots(figsize=(22,6),nrows=1,ncols=ncols)
    for i in range(ncols):
        axs[i].imshow(images[i])
        label = labels[i].squeeze()
        axs[i].set_title(names[int(label)])

show_images(train_images[:8],train_labels[:8],ncols=8)
show_images(train_images[8:16],train_labels[8:16],ncols=8)

# processing
# /255, one hot encoding
def processed_data(images,labels):
    images = np.array(images/255.0,dtype=np.float32)
    labels = np.array(labels,dtype=np.float32)
    return images,labels

train_images,train_labels = processed_data(train_images,train_labels)
test_images,test_labels = processed_data(test_images,test_labels)
train_images[0]

from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

tr_img,val_img,tr_labels,val_labels = train_test_split(train_images,train_labels,
                                                       test_size=0.15,random_state=20)

from tensorflow.keras.layers import Dense,Flatten,Conv2D,Dropout,Activation,MaxPooling2D
from tensorflow.keras.layers import BatchNormalization,GlobalAveragePooling2D,Input
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras.callbacks import ReduceLROnPlateau,EarlyStopping,ModelCheckpoint,LearningRateScheduler

input_tensor = Input(shape=(32,32,3))
# filter : 3x3 필터 개수
# padding = 'same' 원본크기 유지
x = Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu')(input_tensor)
x = Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu')(x)
x = MaxPooling2D(pool_size=(2,2))(x)

x = Conv2D(filters=64,kernel_size=(3,3),padding='same',activation='relu')(x)
x = Conv2D(filters=64,kernel_size=(3,3),padding='same')(x)
x = Activation('relu')(x)
x = MaxPooling2D(pool_size=2)(x)

x = Conv2D(filters=128,kernel_size=(3,3),padding='same',activation='relu')(x)
x = Conv2D(filters=128,kernel_size=(3,3),padding='same',activation='relu')(x)
x = MaxPooling2D(pool_size=2)(x)

x = Flatten(name='flatten')(x)
x = Dropout(rate=0.5)(x)
x = Dense(300,activation='relu',name='fc1')(x)
x = Dropout(rate=0.3)(x)

output = Dense(10,activation='softmax')(x)
model = Model(input_tensor,output)
model.summary()

opt = optimizers.Adam(learning_rate=0.001)
loss = losses.sparse_categorical_crossentropy # sparse 와 차이점: sparse 인코딩 x
model.compile(optimizer=optimizers.Adam(),loss=loss,metrics=['accuracy'])
history = model.fit(train_images,train_labels,batch_size=64,epochs=30,validation_split=0.15)
# validation_split= ,option 데이터 분할하지 않고 가능

import matplotlib.pyplot as plt
def show_history(history):
    plt.figure(figsize=(6,6))
    plt.yticks(np.arange(0,1,0.05))
    plt.plot(history.history['accuracy'],label='train')
    plt.plot(history.history['val_accuracy'],label='valid')
    plt.legend()

show_history(history)
model.evaluate(test_images,test_labels)

