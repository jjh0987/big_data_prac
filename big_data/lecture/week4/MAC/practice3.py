import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 네이버 접속 후 로그인
url = 'http://www.naver.com'
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/chromedriver")

try:
    driver.get(url)
    time.sleep(0.5)
    login = driver.find_element_by_class_name('link_login')
    login.click()
    id = driver.find_element_by_id('id')
    pw = driver.find_element_by_id('pw')
    log_btn = driver.find_element_by_id('log.login')
    id.send_keys('djflswlstlf')
    pw.send_keys('p5kvrm')
    log_btn.click()
except Exception as e:
    print(e)


# capcha 방지
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
# 클립보드 이용 (자동문자 방지 우회)
url = 'http://www.naver.com'
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/chromedriver")

try:
    driver.get(url)
    time.sleep(1)
    link_log = driver.find_element_by_class_name('link_login')
    link_log.click()

    pyperclip.copy(input('id'))
    driver.find_element_by_id('id').send_keys(Keys.COMMAND,'v')
    pyperclip.copy(input('pw'))
    driver.find_element_by_id('pw').send_keys(Keys.COMMAND,'v')
    driver.find_element_by_id('log.login').click()

except Exception as e:
    print(e)
finally:
    print('success')