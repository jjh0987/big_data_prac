import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)
path = '../main/big_data/lecture/week8/data/iris.csv'
columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
df = pd.read_csv(path,names=columns)
