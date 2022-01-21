import requests
import bs4
url = 'https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
res = requests.get(url) # data call
html_str = res.text # write
bs_obj = bs4.BeautifulSoup(html_str,'html.parser') # using bs4 for tag search (data parsing)
movie_list = bs_obj.find_all('img',{'class':'thumb_img'}) # search

img = []
for i in movie_list:
    if len(img) == 5:
        break
    else:
        img.append(i['src']) # width ... etc 속성깂을 호출할 수 있다!
print(img)

j = 0
for i in img:
    j += 1
    pic = requests.get(i)
    pic.raise_for_status()
    with open('big_data/lecture/week3/movie/movie{}.jpg'.format(j),'wb') as f: # write binary (img file)
        f.write(pic.content)
        print('success to save img')
print('check the directory')
