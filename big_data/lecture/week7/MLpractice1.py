from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score,cross_validate
import numpy as np

iris = load_iris()
data_clf = DecisionTreeClassifier(random_state=15)
data = iris.data
label = iris.target
score = cross_val_score(data_clf,data,label,cv=3) # cv : num of folding
print(score)
print(round(np.average(score),4))

score = cross_validate(data_clf,data,label,cv=3)
print(score)

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd
# find proper estimator

x_train,x_test,y_train,y_test = train_test_split(data,label,test_size=0.2,random_state=11)
parameters = {'max_depth':[1,2,3],'min_samples_split':[10,15]} # list of estimator combination
# min_samples_split 로 인해 뎁스가 조절될 수 있다.
# min_samples_split 보다 작은 데이터로 트리 노드가 생성 되지 않게 한다.
grid_dtree = GridSearchCV(data_clf,param_grid=parameters,cv=3,refit=True)
data_clf.get_params().keys()
# dict_keys(['ccp_alpha', 'class_weight', 'criterion',
# 'max_depth', 'max_features', 'max_leaf_nodes',
# 'min_impurity_decrease', 'min_samples_leaf', 'min_samples_split',
# 'min_weight_fraction_leaf', 'random_state', 'splitter'])
grid_dtree.fit(x_train,y_train)

score_df = pd.DataFrame(grid_dtree.cv_results_) # depth 가 너무 높으면 편향 가능성
# parms * cv : num of solit#_test_score
# https://m.blog.naver.com/genesis717/220657683905
score_df[['params','mean_test_score','rank_test_score','split0_test_score','split0_test_score']]
grid_dtree.best_params_
grid_dtree.best_score_
grid_dtree.best_estimator_
grid_dtree.best_index_


from sklearn.metrics import accuracy_score

estimator = grid_dtree.best_estimator_
pred = estimator.predict(x_test)
print(accuracy_score(y_test,pred))


from sklearn.preprocessing import LabelEncoder
items = ['TV','냉장고','전자레인지','컴퓨터','선풍기','선풍기','믹서','믹서']
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
labels = labels.reshape(-1,1)

encoder.classes_
encoder.inverse_transform(labels)

# labels.reshape(len(labels),1) == labels.reshape(-1,1)

# same
from sklearn.preprocessing import OneHotEncoder
one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(labels) # 1개의 컬럼의 모양
oh_labels = one_hot_encoder.transform(labels)
oh_labels.toarray()

df = pd.DataFrame({'item':['TV','냉장고','전자레인지','컴퓨터','선풍기','선풍기','믹서','믹서']})
pd.get_dummies(df)



# normalization, stadardization : feature scailing
iris = load_iris()
iris_data =iris.data
iris_df = pd.DataFrame(data=iris_data,columns=iris.feature_names)
print(iris_df.mean())
print(iris_df.var())

from sklearn.preprocessing import StandardScaler # 정규분포
scalar = StandardScaler()
scalar.fit(iris_df)
iris_scaled = scalar.transform(iris_df)
iris_df_scaled = pd.DataFrame(data=iris_scaled,columns=iris.feature_names)
iris_df_scaled.mean()
iris_df_scaled.var()

from sklearn.preprocessing import MinMaxScaler # x-min / max-min -> 가장 크면 1, 가장 작으면 0
scalar = MinMaxScaler()
scalar.fit(iris_df)
iris_scaled = scalar.transform(iris_df)
iris_df_scaled = pd.DataFrame(data=iris_scaled,columns=iris.feature_names)
iris_df_scaled.min()
iris_df_scaled.max()
iris_df_scaled.mean()


train_arr = np.arange(0,11).reshape(-1,1)
test_arr = np.arange(0,6).reshape(-1,1)
scalar = MinMaxScaler()
scalar.fit(train_arr)
train_scaled = scalar.transform(train_arr)
train_scaled
np.round(train_scaled.reshape(-1),2)

#scalar.fit(test_arr) # 다시 피팅할경우 min max 가 달라지므로 조심한다.
test_scaled = scalar.transform(test_arr)
np.round(test_scaled.reshape(-1),2)
# min max 가 같아야한다. 그래야 0과 1이 이어진다. (test와 train)