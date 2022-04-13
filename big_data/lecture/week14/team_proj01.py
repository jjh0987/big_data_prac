import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
# 가장 저렴한 항공권 찾기

def get_data():
    bs_obj = bs4.BeautifulSoup(driver.page_source)
    data = bs_obj.find_all('p')
    setting = ''
    for i in data:
        setting += i.text
    return setting.replace('\n',' ')

driver = webdriver.Chrome('/Users/junho/Downloads/chromedriver')
url = 'https://www.federalreserve.gov/newsevents/testimony.htm'
driver.get(url)
# 10번째 문서
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').clear()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[2]/div/div[1]/input').send_keys(
    '01012009')
driver.implicitly_wait(2)
# 체크 박스
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[4]/div[1]/label/input').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[4]/div[2]/label/input').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[4]/div[3]/label/input').click()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[4]/div[4]/label/input').click()
driver.implicitly_wait(2)
# submit
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/form/div[5]/a/span').click()
driver.implicitly_wait(2)

article = []
bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('time')
time_table1 = [i.text for i in data]

for i in range(1,21):
    # page in
    driver.find_element_by_xpath(f'//*[@id="article"]/div[1]/div[{i}]/div[2]/p[1]/em/a').click() # 아티클
    article.append(get_data())
    driver.back()# 페이지 아웃


for i in range(1,8):
    # page in
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="article"]/ul[2]/li[3]/a').click()
    time.sleep(0.5)
    driver.find_element_by_xpath(f'//*[@id="article"]/div[1]/div[{i}]/div[2]/p[1]/em/a').click() # 아티클
    time.sleep(1)
    article.append(get_data())
    time.sleep(0.5)
    driver.back() # 페이지 아웃

time.sleep(1)
bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('time')
time_table2 = [i.text for i in data]

time_table = []
time_table.extend(time_table1)
time_table.extend(time_table2)

len(time_table)
len(article)
