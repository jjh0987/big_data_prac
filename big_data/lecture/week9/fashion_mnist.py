import numpy as np
import pandas as pd
from tensorflow.keras.datasets import fashion_mnist


# 28x28 grayscale
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
print(train_images.shape,train_labels.shape)
print(test_images.shape,test_labels.shape)

# mnist visualize
import matplotlib.pyplot as plt
plt.imshow(train_images[0],cmap='gray')
plt.title(train_labels[0])

# image 0
print(train_images[0,:,:])
print(train_labels[0])

class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat',
               'Sandal','Shirt','Sneaker','Back','Ankle boot']
def image_table(row,col,train_images,train_labels):
    for i in range(row*col):
        plt.subplot(row, col, i+1)
        plt.imshow(train_images[i],cmap='gray')
        plt.title(train_labels[i])
        # plt.title(class_names[train_labels[i]])
image_table(2,8,train_images,train_labels)

def show_image(images,labels,ncols=0):
    figure, axs = plt.subplots(figsize=(22,6),nrows=1,ncols=ncols)
    for i in range(ncols):
        axs[i].imshow(images[i],cmap='gray')
        axs[i].set_title(class_names[labels[i]])
show_image(train_images[:8],train_labels[:8],ncols=8)
show_image(train_images[8:16],train_labels[8:16],ncols=8)


def one_hot_encoder(labels):
    one_hot = []
    for label in labels:
        temp = [0 for _ in range(10)]
        temp[label] += 1
        one_hot.append(temp)
    return one_hot
one_hot_labels = np.array(one_hot_encoder(train_labels))


from tensorflow.keras.utils import to_categorical
train_oh_labels = to_categorical(train_labels)
test_oh_labels = to_categorical(test_labels)


def get_processed_data(images,labels):
    return np.array([img/255 for img in images]),labels
scailing_data,labels = get_processed_data(train_images,train_labels)
scailing_data

from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(100,activation='relu'),
    Dense(30,activation='relu'),
    Dense(10,activation='softmax')
])
model.summary()
opt = optimizers.Adam(learning_rate=0.001)
loss = losses.sparse_categorical_crossentropy # sparse 와 차이점: sparse 인코딩 x
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
model.fit(train_images,train_labels,batch_size=200,epochs=30)



from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = Sequential([
    Flatten(input_shape=(28,28)), # vectorize
    Dense(100,activation='relu'),
    Dense(30,activation='relu'),
    Dense(10,activation='softmax')
])
model.summary()
opt = optimizers.Adam(learning_rate=0.001)
loss = losses.categorical_crossentropy # sparse 와 차이점: sparse 인코딩 x
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
history = model.fit(train_images,one_hot_labels,batch_size=200,epochs=30)

print(history.history['loss'])
print(history.history['accuracy'])
pred = model.predict(test_images)

# np.squeeze(arr) : 불필요 차원 축소
extend_pred = model.predict(np.expand_dims(test_images[0],axis=0))
print(np.expand_dims(test_images[0],axis=0).shape)
print(extend_pred.shape)
np.argmax(pred[0])
np.argmax(extend_pred)
# -> automatic : evaluate

model.evaluate(test_images,test_oh_labels,batch_size=64)




# train set 을 train,test 로 분리하여 검증
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

tr_img,val_img,tr_labels,val_labels = train_test_split(train_images,train_labels,
                                                       test_size=0.15,random_state=2021)
tr_label_oh = to_categorical(tr_labels)
val_label_oh = to_categorical(val_labels)

from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = Sequential([
    Flatten(input_shape=(28,28)), # vectorize
    Dense(100,activation='relu'),
    Dense(30,activation='relu'),
    Dense(10,activation='softmax')
])
model.summary()
opt = optimizers.Adam(learning_rate=0.001)
loss = losses.categorical_crossentropy # sparse 와 차이점: sparse 인코딩 x
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
history = model.fit(tr_img,tr_label_oh,batch_size=128,epochs=15,validation_data=(val_img,val_label_oh))

model.evaluate(val_img,val_label_oh,batch_size=64)

print(history.history['loss'])
print(history.history['accuracy'])
print(history.history['val_loss'])
print(history.history['val_accuracy'])
plt.plot(history.history['accuracy'],label='train')
plt.plot(history.history['val_accuracy'],label='valid')
plt.legend()
plt.plot(history.history['loss'],label='train_loss')
plt.plot(history.history['val_loss'],label='valid_loss')
plt.legend()

# representation
# rep1
model = Sequential()
model.add(Flatten(input_shape=(28,28))) # vectorize
model.add(Dense(100,activation='relu'))
model.add(Dense(30,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()

# rep2
from tensorflow.keras.layers import Input,Flatten,Dense
from tensorflow.keras.models import Model
input_tensor = Input(shape=(28,28))
x = Flatten()(input_tensor)
x = Dense(100,activation='relu')(x)
x = Dense(30,activation='relu')(x)
output = Dense(10,activation='softmax')(x)
model = Model(input_tensor,output)
model.summary()