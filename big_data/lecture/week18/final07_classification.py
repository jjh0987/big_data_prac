import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#data = pd.read_csv('/Users/junho/Desktop/data/final_csv/score1.csv').drop('Unnamed: 0',axis=1)
#data.columns
#data.info()


from pykrx import stock
pykrx_df = stock.get_market_ohlcv_by_date(fromdate='2021-04-28', todate='2022-04-28', ticker="035720", adjusted=False)
pykrx = pykrx_df.reset_index()
pykrx.info()
pykrx # idx : 과거 -> 현재

pykrx['종가'].plot()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scale_cols = ['시가', '고가', '저가', '종가', '거래량']
df_scaled = scaler.fit_transform(pykrx[scale_cols])
df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols
df_scaled

TEST_SIZE = 40
WINDOW_SIZE = 10
train = df_scaled[:-TEST_SIZE]
test = df_scaled[-TEST_SIZE:]


def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)


feature_cols = ['시가', '고가', '저가', '거래량']
label_cols = ['종가']

train_feature = train[feature_cols]
train_label = train[label_cols]

# train dataset
train_feature, train_label = make_dataset(train_feature, train_label, 10)

# train, validation set 생성
from sklearn.model_selection import train_test_split
x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.2)

x_train.shape, x_valid.shape
# ((6086, 20, 4), (1522, 20, 4))

test_feature = test[feature_cols]
test_label = test[label_cols]
# test dataset (실제 예측 해볼 데이터)
test_feature, test_label = make_dataset(test_feature, test_label, 10)
test_feature.shape, test_label.shape
# ((180, 20, 4), (180, 1))



from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

model = Sequential()
model.add(LSTM(16,
               input_shape=(train_feature.shape[1], train_feature.shape[2]),
               activation='relu',
               return_sequences=False)
          )
model.add(Dense(1))
