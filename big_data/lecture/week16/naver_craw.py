import time

import pandas as pd
import requests
from selenium import webdriver
import bs4

driver = webdriver.Chrome('/Users/junho/Downloads/chromedriver')
url = 'https://search.naver.com/search.naver?where=news&query=%EC%95%A0%ED%94%8C&sm=tab_opt&sort=1&photo=3&field=0&pd=5&ds=&de=&docid=&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1014&nso=so%3Add%2Cp%3A1y&is_sug_officeid=0'
driver.get(url)


bs_obj = bs4.BeautifulSoup(driver.page_source)
target = bs_obj.find('div', {'class': 'group_news'})
atags = target.find_all('a')
atags
root_path = 'https://www.federalreserve.gov'

a_href = []
for a in atags:
    a_href.append(a['href'])

a_href




time.sleep(2)
number_of_pages = 32
for i in range(number_of_pages):
    bs_obj = bs4.BeautifulSoup(driver.page_source)
    target = bs_obj.find('div', {'id': 'article'})
    atags = target.find_all('a')
    for a in atags:
        if 'item.title' in str(a):
            url = ''
            url = root_path + a['href']
            res = requests.get(url)
            bs_obj = bs4.BeautifulSoup(res.text)
            data = bs_obj.find('div',{'class':'col-xs-12 col-sm-8 col-md-8'})
            it = data.find_all('p') # []
            all = ''
            for dialogue in it:
                #if 'fn1' in str(dialogue):
                #    break
                all += dialogue.text
            writing_list.append(all.replace('\n',' ').replace('\t',' ').replace('\r',' '))
            print(url)
    print(f'page{i+1}')
    time.sleep(2)
    if i < 8:
        driver.find_element_by_xpath('//*[@id="article"]/ul[1]/li[11]/a').click()
    else:
        driver.find_element_by_xpath('//*[@id="article"]/ul[1]/li[8]/a').click()
    time.sleep(1)

len(writing_list)
import pandas as pd
pd.DataFrame(data=writing_list).to_csv('/Users/junho/Downloads/speach.csv')
