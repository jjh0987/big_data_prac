import requests
import bs4

url = f'https://comic.naver.com/webtoon/weekday'
res = requests.get(url) # data call
html_str = res.text # write
bs_obj = bs4.BeautifulSoup(html_str)
# print(bs_obj.body.get_text())
# soup.<tag>.get_text()
# bs_obj.a.attrs
# bs_obj.a['href']
r1 = bs_obj.find('li', {'class': 'rank01'})
r1.a.get_text()
r1.parent.find_all('a') # 상위태그 이용
r1.parent.a.get_text()
r2 = r1.nextSibling.nextSibling
r2.a.get_text()
r2.previousSibling.previousSibling.a.get_text()

r2.next
r2.previous

r1.find_next_sibling('li')
for i in r1.find_next_siblings('li'):
    print(i.get_text())

webtoon = bs_obj.find('a',text='참교육-64화')
webtoons = bs_obj.find_all('a',{'class':'title'})
for toon in webtoons:
    print(toon.text)



max_page = 2
page_toon = []
for page in range(1,max_page+1):
    url = f'https://comic.naver.com/webtoon/list?titleId=786537&page={page}'
    res = requests.get(url)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data = bs_obj.find('table',{'class':'viewList'})
    toon = []
    for i in data.find_all('a'):
        toon.append(i.text+i['href'])
    page_toon.append(toon)
sorted_toon = []
for i in page_toon:
    for j in i:
        sorted_toon.append(j)
sorted_toon.reverse()
myview = [sorted_toon[i] for i in range(0,len(sorted_toon),2)]
for i in myview:
    print(i)
