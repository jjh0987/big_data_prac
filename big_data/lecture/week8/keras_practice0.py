import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)
path = '../main/big_data/lecture/week8/data/ThoraricSurgery.csv'
data_set = np.loadtxt(path,delimiter=',')
X = data_set[:,:17]
Y = data_set[:,17]

print(len(data_set))
model = Sequential()
model.add(Dense(30,input_dim=17,activation='relu'))
model.add(Dense(1,input_dim=17,activation='sigmoid'))

# loss : mse , cross entropy .. , opt : adam,gsd,momentum .. metrics : 리스트 형식도 가능하다.
model.compile(loss='binary_crossentropy',optimizer='adam',metrics='accuracy')
model.fit(X,Y,epochs=10,batch_size=10)
# 1 epochs (data len) 를 batch size 민큼 나누어서
result = model.evaluate(X,Y)


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

path = '../main/big_data/lecture/week8/data/pima-indians-diabetes.csv'
columns = ['pregnant','plasma','pressure','thickness','insulin','BMI','pedigree','age','class']
df = pd.read_csv(path,names=columns)
df.info()
df.describe()
df[['pregnant','class']].groupby('pregnant').mean().sort_values(by='pregnant',ascending=True)
sns.heatmap(df.corr(),annot=True) # vmax : 밝기 조절, cmap : 색상맵핑

grid = sns.FacetGrid(df,col='class')
grid.map(plt.hist,'plasma',bins=10)


X = df.iloc[:,:8]
Y = df.iloc[:,8]
model = Sequential()
model.add(Dense(100,activation='relu'))
model.add(Dense(50,activation='sigmoid'))
model.add(Dense(20,activation='relu'))
model.add(Dense(10,activation='relu'))

model.add(Dense(1,activation='sigmoid'))

opt = tf.keras.optimizers.Adam(lr=0.01)
model.compile(loss='binary_crossentropy',optimizer=opt,metrics='accuracy')
model.fit(X,Y,epochs=50,batch_size=10)

model.evaluate(X,Y)




# catregorical_crossentropy

path = '../main/big_data/lecture/week8/data/iris.csv'
columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
df = pd.read_csv(path,names=columns)
df.info()

X = df.iloc[:,:4]
Y = pd.DataFrame(data=df.iloc[:,4])

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

len(X)
Y,label = encoder(Y)

model = Sequential()
initializer = tf.keras.initializers.HeNormal()

model.add(Dense(10,input_dim=4,activation='sigmoid',kernel_initializer=initializer))

model.add(Dense(15,activation='relu'))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(5,activation='sigmoid'))

model.add(Dense(1,activation='sigmoid'))

opt = tf.keras.optimizers.Adam(lr=0.01)
model.compile(loss='categorical_crossentropy',optimizer=opt,metrics='accuracy')
model.fit(X,Y,epochs=100,batch_size=15)

# model.evaluate(X,Y)