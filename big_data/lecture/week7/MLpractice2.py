import pandas as pd
titanic_train = pd.read_csv('../main/big_data/lecture/week7/data/titanic/train.csv')
titanic_test = pd.read_csv('../main/big_data/lecture/week7/data/titanic/test.csv')
titanic_gender_sub = pd.read_csv('../main/big_data/lecture/week7/data/titanic/gender_submission.csv')
# pclass : 선실등급
# sibsp : 형제자매
# parch : 부모자식
# cabin : 선실
# embarked : 출항지
titanic_train.info()
titanic_train.describe()

titanic_train.isnull().sum()
# titanic_train.isnull().sum().sum()
titanic_train['Age'].fillna(titanic_train['Age'].mean(),inplace=True)
titanic_train['Cabin'].fillna('N',inplace=True)
titanic_train['Embarked'].fillna('N',inplace=True)
titanic_train['Sex'].value_counts()
titanic_train['Cabin'].value_counts()
titanic_train['Embarked'].value_counts()
titanic_train['Cabin'] = titanic_train['Cabin'].str[0]
titanic_train['Cabin'].value_counts()

titanic_pclass = titanic_train['Pclass']
type(titanic_pclass)
titanic_pclass.value_counts()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# jupyter : %matplotlib inline
titanic_df = pd.read_csv('../main/big_data/lecture/week7/data/titanic/train.csv')
titanic_df.head()
titanic_df.groupby('Sex')['Sex'].count()
titanic_df.groupby(['Sex','Survived']).count()
titanic_df.groupby(['Sex','Survived'])['Survived'].count()
sns.barplot(x='Sex',y='Survived',data=titanic_df)

titanic_df.info()
titanic_df.groupby('Survived')['Survived'].count()
sns.barplot(x='Pclass',y='Survived',data=titanic_df)
sns.barplot(x='Sex',y='Survived',data=titanic_df)
sns.barplot(x='Survived',y='Age',data=titanic_df)
sns.barplot(x='SibSp',y='Survived',data=titanic_df)
sns.barplot(x='Parch',y='Survived',data=titanic_df)
sns.barplot(x='Survived',y='Fare',data=titanic_df)
sns.barplot(x='Embarked',y='Survived',data=titanic_df)

sns.barplot(x='Pclass',y='Survived',hue='Sex',data=titanic_df)

category_set = []
for age in titanic_df['Age']:
    if age < 0: category = 'unknown'
    elif age < 12: category = 'child'
    elif age < 18: category = 'teenager'
    elif age < 35: category = 'young adult'
    elif age < 60: category = 'adult'
    else: category = 'elderly'
    category_set.append(category)

group = ['unknown','child','teenager','young adult','adult','elderly']
titanic_df['age_category'] = category_set
sns.barplot(x='age_category',y='Survived',data=titanic_df,hue='Sex',order=group)



def age_category(age):
    if age < 0: category = 'unknown'
    elif age < 12: category = 'child'
    elif age < 18: category = 'teenager'
    elif age < 35: category = 'young adult'
    elif age < 60: category = 'adult'
    else: category = 'elderly'
    return category

titanic_df['age_category'] = titanic_df['Age'].apply(lambda x:age_category(x))
sns.barplot(x='age_category',y='Survived',data=titanic_df,hue='Sex',order=group)

titanic_df.drop('age_category',axis=1,inplace=True)

from sklearn import preprocessing
def encoder(df):
    features = ['Sex','Cabin','Embarked']
    encode = preprocessing.LabelEncoder()
    for feature in features:
        encode.fit(df[feature])
        df[feature] = encode.transform(df[feature])
    return df

titanic_df = encoder(titanic_df)
titanic_df