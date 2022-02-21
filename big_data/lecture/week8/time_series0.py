from fbprophet import Prophet
import numpy as np
import pandas as pd


path = '../main/big_data/lecture/week8/data/avocado.csv'
df = pd.read_csv(path)
df.groupby('type').mean()
df = df.loc[(df.type == 'conventional') & (df.region == 'TotalUS')] # select
data = df[['Date','AveragePrice']].reset_index(drop=True)
data = data.rename(columns={'Date':'ds','AveragePrice':'y'})

# DataFrame 자체에도 플롯기능이 있다.
data.plot(x='ds',y='y',figsize=(16,8))

model = Prophet()
model.fit(data) # 어떯게 작동되나..?
future = model.make_future_dataframe(periods=365) # dt = 1
forecast = model.predict(future)
forecast
# data 뒤에 period 길이만큼 데이터 추가

model.plot(forecast)
model.plot_components(forecast)