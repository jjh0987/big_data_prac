import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression # 앙상블 조합용
from sklearn.neighbors import KNeighborsClassifier # 앙상블 조합용
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
cancer_data = cancer.data
cancer_label = cancer.target
cancer_label
data_df = pd.DataFrame(cancer.data,columns=cancer.feature_names)

lr_clf = LogisticRegression()
knn_clf = KNeighborsClassifier(n_neighbors=8)
vo_clf = VotingClassifier(estimators=[('LR',lr_clf),('KNN',knn_clf)],voting='soft')

X_train,X_test,y_train,y_test = train_test_split(
    cancer_data,cancer_label,test_size=0.2,random_state=156
)

vo_clf.fit(X_train,y_train)
pred = vo_clf.predict(X_test)
print(accuracy_score(pred,y_test))

classfiers = [lr_clf,knn_clf]
acc_list = []
for classfier in classfiers:
    clf = classfier
    clf.fit(X_train,y_train)
    pred = classfier.predict(X_test)
    acc = acc_list.append(accuracy_score(pred,y_test))
print(classfiers)
print(acc_list)


#
import pandas as pd
import matplotlib.pyplot as plt

path = '../main/big_data/lecture/week7/data/human_activity/features.txt'
feature_name_df = pd.read_csv(path,sep='\s+',header=None,names=['column_index','column_name'])
feature_name_df.groupby('column_name').count()
len(feature_name_df) # 561
feature_dup_df = feature_name_df.groupby('column_name').count()
feature_dup_df[feature_dup_df['column_index'] > 1].count()
feature_dup_df[feature_dup_df['column_index'] == 1].count()

# 같은 컬럼명에 대해서 인덱싱
def get_new_feature_name_df(old_feature_name_df):
    feature_dup_df = pd.DataFrame(data=old_feature_name_df.groupby('column_name').cumcount(),
                                  columns=['dup_cnt'])
    feature_dup_df = feature_dup_df.reset_index()
    new_feature_name_df = pd.merge(old_feature_name_df.reset_index(),feature_dup_df,how='outer')
    new_feature_name_df['column_name'] = new_feature_name_df[['column_name','dup_cnt']].apply(
        lambda x: x[0]+'_'+str(x[1]) if x[1] > 0 else x[0],axis=1
    )
    new_feature_name_df = new_feature_name_df.drop(['index'],axis=1)
    return new_feature_name_df

def get_human_dataset():
    path = '../main/big_data/lecture/week7/data/human_activity/features.txt'
    feature_name_df = pd.read_csv(path, sep='\s+', header=None, names=['column_index', 'column_name'])
    new_feature_name_df = get_new_feature_name_df(feature_name_df)

    feature_name = new_feature_name_df.iloc[:,1].values.tolist() # call column idx 1 - 561
    X_train = pd.read_csv('../main/big_data/lecture/week7/data/human_activity/train/X_train.txt',sep='\s+'
                          ,names=feature_name) # names : col names
    y_train = pd.read_csv('../main/big_data/lecture/week7/data/human_activity/train/y_train.txt',sep='\s+'
                          ,header=None,names=['label'])
    X_test = pd.read_csv('../main/big_data/lecture/week7/data/human_activity/test/X_test.txt',sep='\s+'
                          ,names=feature_name)
    y_test = pd.read_csv('../main/big_data/lecture/week7/data/human_activity/test/y_test.txt',sep='\s+'
                          ,header=None,names=['label'])
    return X_train,X_test,y_train,y_test
X_train,X_test,y_train,y_test = get_human_dataset()

from sklearn.ensemble import RandomForestClassifier
import warnings
rf_clf = RandomForestClassifier(random_state=0)
rf_clf.fit(X_train,y_train)
pred = rf_clf.predict(X_test)
acc = accuracy_score(pred,y_test)
print(acc)

from sklearn.model_selection import GridSearchCV
# parms = {'n_estimators':[],'max_depth':[],'min_samples_split':[],'min_samples_leaf':[]}
parms = {'n_estimators':list(range(30,80,5)), # num of iter : using classifier
         'max_depth':list(range(9,15,3)),
         'min_samples_split':[2],
         # 'learning_rate': [0.1], # invalid ?
         'min_samples_leaf':list(range(2,8,2))}
rf_clf = RandomForestClassifier(random_state=0,n_jobs=-1) # n_jobs ?
grid_cv = GridSearchCV(rf_clf,param_grid=parms,cv=2,n_jobs=-1,)
grid_cv.fit(X_train,y_train)
print(grid_cv.best_params_)
print(round(grid_cv.best_score_,4))

# cv : 10
{'max_depth': 15, 'min_samples_leaf': 6, 'min_samples_split': 2, 'n_estimators': 45}
0.9361

from sklearn.ensemble import GradientBoostingClassifier
import time
import warnings
X_train,X_test,y_train,y_test = get_human_dataset()
start_time = time.time()

gb_clf = GradientBoostingClassifier(random_state=0)
gb_clf.fit(X_train,y_train)
pred = gb_clf.predict(X_test)
acc = accuracy_score(pred,y_test)
print(acc)
print(time.time()-start_time)


gb_clf = GradientBoostingClassifier(random_state=0)
parms = {'n_estimators':[30],
         'learning_rate':[0.05,0.1]}
grid_cv =GridSearchCV(gb_clf,param_grid=parms,cv=2,verbose=1)
grid_cv.fit(X_train,y_train)
pred = grid_cv.best_estimator_.predict(X_test)
acc = accuracy_score(pred,y_test)
print(acc)