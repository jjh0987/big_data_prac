import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
titanic_df = pd.read_csv('../main/big_data/lecture/week7/data/titanic/train.csv')
# titanic_test = pd.read_csv('../main/big_data/lecture/week7/data/titanic/test.csv')
# titanic_gender_sub = pd.read_csv('../main/big_data/lecture/week7/data/titanic/gender_submission.csv')

# null
titanic_df['Age'].fillna(titanic_df['Age'].mean(),inplace=True)
titanic_df['Cabin'].fillna('N',inplace=True)
titanic_df['Embarked'].fillna('N',inplace=True)
features = ['Sex', 'Cabin', 'Embarked','Survived']

# labeling
from sklearn import preprocessing
def encoder(df):
    features = ['Sex','Cabin','Embarked']
    encode = preprocessing.LabelEncoder()
    for feature in features:
        encode.fit(df[feature])
        df[feature] = encode.transform(df[feature])
    return df

titanic_df = encoder(titanic_df)
titanic_df = titanic_df[features]
y_titanic_df = titanic_df['Survived']
x_titanic_df = titanic_df.drop('Survived',axis=1)
x_titanic_df

# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x_titanic_df,y_titanic_df,test_size=0.2,random_state=11)
# y_train
'''
class feature_encoding():
    def __init__(self):
        pass
    
    def fill_na(df):
        pass

    def drop_features(df):
        pass

    def format_features(df):
        pass

    def transform_features(df):
        # df = fill_na(df)
        # df = drop_features(df)
        # df = format_features(df)
        # return df
        pass
'''

dt_clf = DecisionTreeClassifier(random_state=11)
rf_clf = RandomForestClassifier(random_state=11)
lr_clf = LogisticRegression()

estimator = [dt_clf,rf_clf,lr_clf]

from sklearn.model_selection import StratifiedKFold
# df_clf.fit(x_train,y_train)
# pred = df_clf.predict(x_test)
# accuracy_score(y_test,pred)
def bundle_skf(data,label,n_split,estimator):
    skf = StratifiedKFold(n_splits=n_split)
    cv_acc = [[],[],[]]
    for train_index,test_index in skf.split(data,label):
        '''
        label_train = y_train
        label_test = y_test
        print('train')
        print(label_train.value_counts())
        print('test')
        print(label_test.value_counts())
        '''
        x_train, x_test = data.iloc[train_index],data.iloc[test_index]
        y_train, y_test = label.iloc[train_index],label.iloc[test_index]

        i = 0
        for clf in estimator:
            clf.fit(x_train, y_train)  # classifier
            pred = clf.predict(x_test)

            acc = np.round(accuracy_score(y_test, pred), 4)
            cv_acc[i].append(acc)
            i += 1
    return cv_acc

cv_acc = bundle_skf(x_titanic_df,y_titanic_df,5,estimator)
for i,j in zip(estimator,cv_acc):
    print(f'{i} :',round(np.average(j),4))

from sklearn.model_selection import cross_val_score
score = cross_val_score(dt_clf,x_titanic_df,y_titanic_df,cv=5)
score
round(np.mean(score),4)