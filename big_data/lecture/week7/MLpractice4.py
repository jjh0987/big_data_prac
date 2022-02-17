import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
items = ['a','b','c','d']
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
labels = labels.reshape(-1,1)

encoder = OneHotEncoder()
encoder.fit(labels)
oh_labels = encoder.transform(labels)
data_label = oh_labels.toarray()

from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


iris = load_iris()
print(iris)
iris_data = iris.data # feature : 꽃받침 길이,꽃받침 너비,꽃입 길이,꽃입 너비
iris_data = iris_data[:,[2,3]]

iris_label = iris.target
columns = iris.target_names
x_train,x_test,y_train,y_test = train_test_split\
    (iris_data,iris_label,test_size=0.3,random_state=1,stratify=1)
# stratify=y ?
# cv = ShuffleSplit(n_splits=1,test_size=0.3,random_state=1)

np.bincount(y_train)
np.bincount(y_test)

sc = StandardScaler()
sc.fit(x_train)
X_train_std = sc.transform(x_train)
X_test_std = sc.transform(x_test)

ppn = Perceptron(eta0=0.1,random_state=1)
ppn.fit(X_train_std,y_train)
pred = ppn.predict(X_test_std)
accuracy_score(pred,y_test)

print(sum(pred != y_test))