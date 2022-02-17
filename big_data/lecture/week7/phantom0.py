from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4

# PhantomJS 모듈의 WebDriver 객체를 생성합니다.
driver = webdriver.PhantomJS()
driver.set_window_size(2560,1440)

# Google 메인 페이지를 엽니다.
url = 'https://www.jumpit.co.kr/positions?jobCategory=19&jobCategory=8'
driver.get(url)
print('finish')

# 타이틀에 'Google'이 포함돼 있는지 확인합니다.
# assert 'Google' in driver.title

# 검색어를 입력하고 검색합니다.
# input_element = driver.find_element_by_name('q')
# input_element.send_keys('Python')
# input_element.send_keys(Keys.RETURN)

# 타이틀에 'Python'이 포함돼 있는지 확인합니다.
# assert 'Python' in driver.title

# 스크린샷을 찍습니다.
# driver.save_screenshot('search_results.png')
driver.title
data = driver.page_source

bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('div')
for i in data:
    print(i.text)


driver.close()
# check window
import dryscrape
