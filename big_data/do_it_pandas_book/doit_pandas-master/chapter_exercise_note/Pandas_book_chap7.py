# 07-1
import pandas
import pandas as pd

pew = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/pew.csv")
pew.shape
pew.head()
pew.iloc[:,0:6]
pew_long = pd.melt(pew,id_vars='religion') # 다중컬럼 입력가능
pew_long = pd.melt(pew,id_vars='religion',var_name='income',value_name='count')
pew_long
pew_temp = pd.melt(pew,value_vars='religion')
pew_temp

# 07-2
ebola = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/country_timeseries.csv")
ebola.columns
ebola.head()
ebola
ebola_long = pd.melt(ebola,id_vars=['Date','Day'])
ebola_long
variable_split = ebola_long.variable.str.split('_')
variable_split
type(variable_split)
type(variable_split[0])
variable_split[0]
variable_split.str[0]
status_value = variable_split.str.get(0) # status
country_value = variable_split.str.get(1) # country
ebola_long['status'] = status_value
ebola_long['country'] = country_value
ebola_long.head()
ebola_long = ebola_long.drop(columns='variable')
ebola_long.shape
ebola.shape

ebola_long
subset = ebola_long.iloc[:122,[1,2]]
subset_x = subset.iloc[:,0]
subset_y = subset.interpolate().iloc[:,1]
from matplotlib import pyplot as plt
plt.plot(subset_x,subset_y)
plt.title('Guinea daily cases')

# 07-3
weather = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/weather.csv")
weather_melt = pd.melt(weather,id_vars=['id','year','month','element'],var_name='day',value_name='temperature')
weather_melt
weather_tie = weather_melt.pivot_table(index=['id','year','month','day'],columns='element',values='temperature',dropna=False)
weather_tie.reset_index()
weather_tie.iloc[:31,:]

# 07-4
billboard = pd.read_csv("../main/big_data/do_it_pandas_book/doit_pandas-master/chapter_exercise_note/data/billboard.csv")
billboard.columns
billboard_long = pd.melt(billboard,id_vars=['year','artist','track','time','date.entered'],var_name='week',value_name='rating')
billboard_long.columns
billboard_long[billboard_long.track == 'Loser']
billboard_song = billboard_long[['year','artist','track','time']]
billboard_songs = billboard_song.drop_duplicates() # 중복제거
billboard_songs['id'] = range(len(billboard_songs))
billboard_rating = billboard_long.merge(billboard_songs,on=['year','artist','track','time'])
billboard_rating

# 07-5
# skip