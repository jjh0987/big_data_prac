from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 네이버 접속 후 로그인창 누르고 뒤로가기
url = 'http://www.naver.com'
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/MAC/chromedriver")
driver.get(url)
elements = driver.find_element_by_class_name('link_Login')
elements.click()
driver.back()

# a 태그 링크 프린트
elements = driver.find_elements_by_tag_name('a')
for idx,e in enumerate(elements):
    print(e.get_attribute('href'))

# 다음 접속 후 '인기영화' 검색
url = 'https://www.daum.net/'
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/MAC/chromedriver")
driver.get(url)
elements = driver.find_element_by_id('q')
elements.send_keys('인기영화')
elements.send_keys(Keys.ENTER)


elements = driver.find_element_by_id('q')
elements.send_keys('인기영화')
element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
element.click()
driver.close()
driver.quit()