# 5년치 포스터 다운 받기

import requests
import bs4

movie_list = []
year = 2022
for i in range(1,6):
    url = 'https://search.daum.net/search?w=tot&q='+f'{year-i}'+'%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    html_src = requests.get(url)
    html_str = html_src.text
    bs_obj = bs4.BeautifulSoup(html_str,'html.parser')
    movie_list.append(bs_obj.find_all('img', {'class': 'thumb_img'}))

img = []
for year_movie in movie_list:
    year_img = []
    for movie in year_movie:
        if len(year_img) == 5:
            break
        else:
            year_img.append(movie['src'])
    img.append(year_img)

num_year = 0
for i in img:
    num_year += 1
    num = 0
    for j in i:
        num += 1
        pic = requests.get(j)
        pic.raise_for_status()
        with open(f'big_data/lecture/week3/movie/movie{year-num_year}_{num}.jpg','wb') as f: # write binary
            f.write(pic.content)
        print('success to save img')
print('check the save directory')

import selenium
import webdriver_manager