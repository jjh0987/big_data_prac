# import sklearn
# print(sklearn.__version__)
# 붓꽃 품종 예상
# 알고리즘 : 의사결정트리 (descision tree)
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import pandas as pd

iris = load_iris()
print(iris)
iris_data = iris.data # feature : 꽃받침 길이,꽃받침 너비,꽃입 길이,꽃입 너비
iris_target = iris.target
iris.target_names
len(iris_data)

# test_size 20%
x_train,x_test,y_train,y_test = train_test_split(iris_data,iris_target,test_size=0.2,random_state=11)
x_test
df_clf = DecisionTreeClassifier(random_state=11) # 분류모델
df_clf.fit(x_train,y_train)
pred = df_clf.predict(x_test)
accuracy_score(y_test,pred)

dt_clf = DecisionTreeClassifier(random_state=100)
kfold = KFold(n_splits=5) # 5분할 데이터
cv_acc = []

n_iter = 0
for train_index, test_index in kfold.split(iris_data):
    # print(train_index)
    # print(test_index)
    # iris_data : data set
    # iris_target : answer label

    x_train,x_test = iris_data[train_index],iris_data[test_index]
    y_train,y_test = iris_target[train_index],iris_target[test_index]

    df_clf.fit(x_train,y_train) # classifier
    pred = df_clf.predict(x_test)
    n_iter += 1

    acc = np.round(accuracy_score(y_test,pred),4)
    train_size = x_train.shape[0]
    test_size = x_test.shape[0]
    cv_acc.append(acc)
    print(n_iter,acc,train_size,test_size)
    print(n_iter,test_index)

print(np.mean(cv_acc))

iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
iris_df
iris_df['label'] = iris_target
iris_df['label'].value_counts()

# data bias
kfold = KFold(n_splits=3,shuffle=True) # shuffle option
kfold
n_iter = 0
for train_index,test_index in kfold.split(iris_df): # y?
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('train')
    print(label_train.value_counts())
    print('test')
    print(label_test.value_counts())



from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=3) # 3분할 데이터에서 골고루 사용
n_iter = 0

for train_index,test_index in skf.split(iris_df,iris_df['label']):
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('train')
    print(label_train.value_counts())
    print('test')
    print(label_test.value_counts())




df_clf = DecisionTreeClassifier(random_state=156) # random seed
skf = StratifiedKFold(n_splits=3)
n_iter = 0
iris = load_iris()
features = iris.data
label = iris.target
cv_acc = []

iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
iris_df['label'] = iris_target
iris_df
for train_index,test_index in skf.split(features,label):
    # print(train_index)
    # print(test_index)
    # iris_data : data set
    # iris_target : answer label
    distribution = iris_df['label'].iloc[train_index]
    x_train, x_test = iris_data[train_index], iris_data[test_index]
    y_train, y_test = iris_target[train_index], iris_target[test_index]

    df_clf.fit(x_train, y_train)  # classifier
    pred = df_clf.predict(x_test)
    n_iter += 1

    acc = np.round(accuracy_score(y_test, pred), 4)
    train_size = x_train.shape[0]
    test_size = x_test.shape[0]
    cv_acc.append(acc)
    print(n_iter, acc, train_size, test_size)
    print(test_index)
    print(distribution.value_counts())

print(np.mean(cv_acc))
print(np.round(cv_acc,4))
cv_acc