import pandas as pd
test = pd.read_csv('/Users/junho/Downloads/카카오뉴스기사_최종.csv')
fear_greed_score = test.loc[:,['날짜','fear/greed']]

temp = fear_greed_score.groupby('날짜').mean()['fear/greed']
temp = pd.DataFrame(temp)
temp = temp.reset_index()
temp.plot()

from pykrx import stock
pykrx_df = stock.get_market_ohlcv_by_date(fromdate='2021-04-30', todate='2022-04-29', ticker="035720", adjusted=False)
pykrx = pykrx_df.reset_index()
pykrx['종가'].plot()
pykrx['등락률'].plot()

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(temp['fear/greed'])
plt.subplot(1,3,2)
plt.plot(pykrx['종가'])
plt.subplot(1,3,3)
plt.plot(pykrx['등락률'].plot())


