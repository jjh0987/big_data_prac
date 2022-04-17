from calendar import month_abbr
from unicodedata import name
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings(action='ignore')

## 연준 멤버 이름 크롤링
month_ab = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
url = 'https://www.federalreserve.gov/aboutthefed/bios/board/boardmembership.htm'
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, 'html.parser')
article = soup.find('tbody') # {'class': 'col-xs-12 col-sm-8 col-md-8'}
htmls = article.find_all('a')
