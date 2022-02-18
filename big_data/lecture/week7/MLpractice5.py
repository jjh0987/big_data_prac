import pandas as pd
import matplotlib.pyplot as plt

path = '../main/big_data/lecture/week7/data/human_activity/features.txt'
feature_name_df = pd.read_csv(path,sep='\s+',header=None,names=['column_index','column_name'])
feature_name_df.groupby('column_name').count()
len(feature_name_df) # 561
feature_dup_df = feature_name_df.groupby('column_name').count()
feature_dup_df[feature_dup_df['column_index'] > 1].count()
feature_dup_df[feature_dup_df['column_index'] == 1].count()


'''
old_feature_name_df = feature_name_df
old_feature_name_df
feature_dup_df = pd.DataFrame(data=old_feature_name_df.groupby('column_name').cumcount(),
                                  columns=['dup_cnt'])
feature_dup_df

feature_dup_df = feature_dup_df.reset_index()
feature_dup_df
new_feature_name_df = pd.merge(old_feature_name_df.reset_index(),feature_dup_df,how='outer')
new_feature_name_df

new_feature_name_df['column_name'] = new_feature_name_df[['column_name','dup_cnt']].apply(
    lambda x: x[0]+'_'+str(x[1]) if x[1] > 0 else x[0],axis=1
)
new_feature_name_df = new_feature_name_df.drop(['index'],axis=1)
new_feature_name_df
'''

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
X_train.shape # 7352, 561 -> 길이, 특성수
print(y_train['label'].value_counts()) # 1 - 6

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
dt_clf = DecisionTreeClassifier(random_state=156)
dt_clf.fit(X_train,y_train)
pred = dt_clf.predict(X_test)
acc = accuracy_score(pred,y_test)
print(round(acc,4))
print(dt_clf.get_params())

from sklearn.model_selection import GridSearchCV
parm = {'max_depth':[6,8,12,16],'min_samples_split':[16,24]}
grid_cv = GridSearchCV(dt_clf,param_grid=parm,scoring='accuracy',cv=5,verbose=1)
# verbose : show fitting condition
grid_cv.fit(X_train,y_train)
print(grid_cv.best_params_)
print(round(grid_cv.best_score_,4))
cv_result = pd.DataFrame(grid_cv.cv_results_)
grid_cv.cv_results_

import seaborn as sns
best_clf = grid_cv.best_estimator_
best_clf.fit(X_train,y_train)
importance_value = best_clf.feature_importances_
importance_value_series = pd.Series(importance_value,index=X_train.columns)
mapping = importance_value_series.sort_values(ascending=False)[:20]
sns.barplot(x=mapping,y=mapping.index)
