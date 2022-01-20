import folium
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'..\big_data\lecture\week3\data\seoul.csv','r',encoding='cp949')
temp = []
i = 0
while i < len(df):
    temp.append(df.iloc[i][0].split(','))
    i += 1

DF = pd.DataFrame(temp,columns=['DATE','LOCATION','MEAN','MIN','MAX'])
high = DF[['MAX']]
plot_high = []
for i in range(len(high)):
    plot_high.append(float(high.loc[i,'MAX']))
plt.plot(plot_high)

extract_birth = []
for i in range(len(DF)):
    if DF.loc[i,'DATE'].split('-')[1] == '01' and DF.loc[i,'DATE'].split('-')[2] == '01':
        extract_birth.append(DF.loc[i,:])
print(extract_birth)

extract_birth_temp = []
for i in range(len(DF)):
    if DF.loc[i,'DATE'].split('-')[1] == '01' and DF.loc[i,'DATE'].split('-')[2] == '01':
        extract_birth_temp.append(float(DF.loc[i,'MIN']))
print(extract_birth_temp)

# 한글 타이틀
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 한글화 경우, 마이너스 깨짐 방지.
plt.plot(plot_high)
plt.title('일별 최고온도')

