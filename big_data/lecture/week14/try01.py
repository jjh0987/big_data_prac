import time

import pandas as pd
import requests
from selenium import webdriver
import bs4

driver = webdriver.Chrome('/Users/junho/Downloads/chromedriver')
url = 'https://www.federalreserve.gov/newsevents/testimony.htm'
driver.get(url)
driver.implicitly_wait(2)
driver.set_window_size(2560, 1440)
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').clear()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').send_keys(
    '04/20/1992')
driver.implicitly_wait(2)

# submit
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[5]/a/span').click()
driver.implicitly_wait(2)
writing_list = []
root_path = 'https://www.federalreserve.gov'
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
