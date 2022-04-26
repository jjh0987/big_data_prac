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
    '07/01/1992')
driver.implicitly_wait(2)

# submit
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[5]/a/span').click()
driver.implicitly_wait(2)
writing_list = []
bs_obj = bs4.BeautifulSoup(driver.page_source)
'''
time_tags = bs_obj.find_all('time', {'class': 'itemDate ng-binding'})
time_data = [i.text for i in time_tags]
time_data
'''
time_data = []
root_path = 'https://www.federalreserve.gov'
time.sleep(2)
cnt = 0
for i in range(13):
    bs_obj = bs4.BeautifulSoup(driver.page_source)
    target = bs_obj.find('div', {'id': 'article'})
    atags = target.find_all('a')
    time_tags = bs_obj.find_all('time', {'class': 'itemDate ng-binding'})
    for j in time_tags:
        if j.text == '9/25/2019':
            cnt += 1
            if cnt == 2:
                time_data.append(j.text)
        else:
            time_data.append(j.text)
    for a in atags:
        if 'item.title' in str(a):
            try:
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
            except:
                pass
    print(f'page{i+1}')
    time.sleep(4)
    if i < 8:
        driver.find_element_by_xpath('//*[@id="article"]/ul[1]/li[11]/a').click()
    else:
        driver.find_element_by_xpath('//*[@id="article"]/ul[1]/li[8]/a').click()
    time.sleep(1)

len(writing_list)
len(time_data)
df = pd.DataFrame()
df['date'] = time_data
df['target'] = writing_list
df.to_csv('/Users/junho/Downloads/testimony2010-2022.csv')