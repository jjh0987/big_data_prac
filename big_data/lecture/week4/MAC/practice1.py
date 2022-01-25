import requests
import bs4
import pandas

max_page = 2
page_toon = []
page_star = []
for page in range(1,max_page+1):
    url = f'https://comic.naver.com/webtoon/list?titleId=786537&page={page}'
    res = requests.get(url)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data = bs_obj.find('table',{'class':'viewList'})
    toon = []
    star = []
    for i in data.find_all('a'):
        toon.append(i.text+i['href'])
    for i in data.find_all('strong'):
        star.append(i.text)
    page_toon.append(toon)
    page_star.append(star)
sorted_toon = []
sorted_star = []
for i in page_toon:
    for j in i:
        sorted_toon.append(j)
for i in page_star:
    for j in i:
        sorted_star.append(j)
sorted_toon.reverse()
sorted_star.reverse()
myview = [sorted_toon[i] for i in range(0,len(sorted_toon),2)]
mystar = [float(i) for i in sorted_star]
for i in myview:
    print(i)

data = []
for i in range(len(sorted_star)):
    data.append([myview[i],mystar[i]])

df = pandas.DataFrame(data=data,columns=['contents','evaluation'])
sum(df.loc[:,'evaluation'])



import requests
import bs4
import pandas

max_page = 2
page_toon = []
page_star = []
for page in range(1,max_page+1):
    url = f'https://comic.naver.com/webtoon/list?titleId=786537&page={page}'
    res = requests.get(url)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data = bs_obj.find_all('div',{'class':'rating_type'})
    for star in data:
        print(star.strong.text)
