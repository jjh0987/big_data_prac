from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4



# PhantomJS 모듈의 WebDriver 객체를 생성합니다.
path = '/Users/junho/Desktop/main/big_data/lecture/week7/phantomjs-2.1.1-macosx/bin/phantomjs'
driver = webdriver.PhantomJS(executable_path=path)
# driver.get('https://www.google.co.kr/')
# driver.title
# driver.save_screenshot('google.png') # 최상위 작업공간에 스크린샷 저장 : main


driver.get('https://www.jumpit.co.kr/position/6738')
# driver.set_window_size(800,600)
data = driver.find_element_by_tag_name('body')

driver.execute_script()

driver.clear()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4

# PhantomJS 모듈의 WebDriver 객체를 생성합니다.
path = '/Users/junho/Desktop/main/big_data/lecture/week7/phantomjs-2.1.1-macosx/bin/phantomjs'
driver = webdriver.PhantomJS(path)
# Google 메인 페이지를 엽니다.
driver.get('https://www.google.co.kr/')

# 타이틀에 'Google'이 포함돼 있는지 확인합니다.
print(driver.title)

# 검색어를 입력하고 검색합니다.
input_element = driver.find_element_by_name('q')
input_element.send_keys('python')
input_element.send_keys(Keys.RETURN)

# 타이틀에 'Python'이 포함돼 있는지 확인합니다.
print(driver.title)
# 스크린샷을 찍습니다.
# driver.save_screenshot('search_results.png')
bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('h3')
for i in data:
    print(i.text)
driver.close()
'''
from bs4 import BeautifulSoup
import requests

url = 'https://www.jumpit.co.kr/position/6738'
engine = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
headers = {'User-Agent': engine}
res = requests.get(url, headers=headers)
html_str = res.text
data = BeautifulSoup(html_str)
data.text
'''