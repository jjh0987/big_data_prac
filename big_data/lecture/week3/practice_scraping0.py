import requests
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
import bs4
# crawling : craw data
# parsing : contents extract
# http://url/http # 에러 구분

url = 'http://www.kakakaaisdjoiasjdioasjk.com/kim.html'
html = urlopen(url)
res = requests.get('http://naver.com')
#res = requests.get('http://yyy.tistory.com'

print('status_code :',res.status_code)
if res.status_code == requests.codes.ok:
    print('success')
else:
    print('fail')

res.raise_for_status() # 404 이면 에러가 나온다.
# 400- client error , 500- server error
print('success')
print(len(res.text))
res.text # html 소스 전문을 받아 온다.

print(html.read()) # requests 와 다르게 read를 해야 읽어 온다. requests.get 은 실행 시 바로 가져 온다.
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print('success')
#----------------------------

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>"""
bs_obj = bs4.BeautifulSoup(html_str,'html.parser')
print(type(bs_obj))
ul = bs_obj.find('ul')
li = ul.find('li')
print(li.text)

li = ul.find_all('li')
for check in li:
    print(check.text)

html_str1 = '''
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>hel</li>
            <li>bye</li>
            <li>wel</li>
        </ul>
    </body>
</html>
'''
bs_obj1 = bs4.BeautifulSoup(html_str1,'html.parser')
reply_class_ul = bs_obj1.find('ul',{'class':'reply'})
print(reply_class_ul)
list_of_li = reply_class_ul.find_all('li')
for check in list_of_li:
    print(check.text)


html_str2 = '''
<html>
    <body>
        <ul class="ko">
            <li>
                <a herf="www.naver.com">naver</a>
            </li>
            <li>
                <a herf="www.daum.net">daum</a>
            </li>
        </ul>
        <ul class="sns">
            <li>
                <a herf="www.google.com">google</a>
            </li>
            <li>
                <a herf="www.facebook.com">facebook</a>
            </li>
        </ul>
    </body>
</html>'''
bs_obj2 = bs4.BeautifulSoup(html_str2,'html.parser')
ultag = bs_obj2.find_all('ul')
for i in ultag:
    print(i.find_all('a'))
atag = ultag[0].find_all('a')
print(atag)
print(atag[0]['herf'])