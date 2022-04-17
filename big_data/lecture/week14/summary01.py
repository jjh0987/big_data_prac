import pandas as pd
beigebook = pd.read_csv('/Users/junho/Desktop/main/big_data/lecture/week14/beigebook2002-2022.csv')
testimony = pd.read_csv('/Users/junho/Desktop/main/big_data/lecture/week14/testimony2009-2022.csv')
# from transformers import pipeline
# qa = pipeline('question-answering')

# qa(question='Will interest rates rise?',context=testimony.iloc[0,1])


import nltk
nltk.__version__
from nltk.tokenize import word_tokenize
word_tokenize(beigebook.iloc[0,1])