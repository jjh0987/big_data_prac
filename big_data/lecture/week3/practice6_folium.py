import folium
import pandas as pd
import json

seoul0 = folium.Map(location=[37.55,126.98],zoom_start=10)
seoul0.save(r'..\big_data\lecture\week3\seoul0.html')

seoul1 = folium.Map(location=[37.55,126.98],tiles='Stamen Terrain',zoom_start=10)
seoul1.save(r'..\big_data\lecture\week3\seoul1.html')
folium.Map()

df = pd.read_excel(r'..\big_data\lecture\week3\data\folium_data\서울지역 대학교 위치.xlsx') # 학교 좌표 등
df.columns = ['학교','위도','경도']
df.식당 = 'ㅋㅋ'

seoul2 = folium.Map(location=[37.55,126.98],tiles='Stamen Terrain',zoom_start=10)
for name,lat,lng in zip(df.index,df.위도,df.경도):
    folium.Marker((lat,lng),popup=name).add_to(seoul2)
seoul2.save(r'..\big_data\lecture\week3\seoul2.html')

seoul3 = folium.Map(location=[37.55,126.98],tiles='Stamen Terrain',zoom_start=10)
for name,lat,lng in zip(df.학교,df.위도,df.경도):
    iframe = folium.IFrame(name,width=50,height=150) # frame default setting
    popup = folium.Popup(iframe,max_width=50) # popup box
    folium.CircleMarker((lat,lng)
                        ,radius=10
                        ,color='brown' # 둘레 색
                        ,fill=True
                        ,fill_color='coral' # 채우는 색
                        ,fill_capacity=0.7 # 투명도
                        ,popup=popup).add_to(seoul3) # popup:선택시 해당 데이터 출력
seoul3.save(r'..\big_data\lecture\week3\seoul3.html')
# ------------------------------------
file_path = r'..\big_data\lecture\week3\data\folium_data\경기도인구데이터.xlsx'
df = pd.read_excel(file_path,index_col='구분')
df.columns = df.columns.map(str)
geo_path = r'..\big_data\lecture\week3\data\folium_data\경기도행정구역경계.json'
try:
    geo_data = json.load(open(geo_path,encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path,encoding='utf-8-sig'))

g_map = folium.Map(location=[37.5502,126.982],
                   tiles='Stamen Terrain',
                   zoom_start=9)
year = '2007' # 2007 ~ 2017
folium.Choropleth(geo_data=geo_data,
                  data = df[year],
                  fill_color='YlOrRd',
                  fill_opacity=0.7,
                  line_opacity=0.7,
                  threshold_scale=[10000,100000,300000,500000,700000],
                  key_on='feature.properties.name',
                  ).add_to(g_map)
g_map.save(r'..\big_data\lecture\week3\population %s.html'%year)