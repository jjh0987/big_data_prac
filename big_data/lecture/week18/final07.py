import pandas as pd
data = pd.read_csv('/Users/junho/Desktop/data/final_csv/score1.csv').drop('Unnamed: 0',axis=1)
data.columns
data.info()