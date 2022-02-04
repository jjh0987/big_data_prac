import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://naver.com'
driver = webdriver.Chrome(r'C:\Users\xcom2\git_bash_practice\big_data\lecture\week4\chromedriver.exe')

try:
    driver.get(url)
    time.sleep(1)
    login = driver.find_element_by_class_name('link_login')
    login.click()

    id = driver.find_element_by_id('id')
    password = driver.find_element_by_id('pw')
    pyperclip.copy('djflswlstlf')
    id.send_keys(Keys.CONTROL,'v')
    pyperclip.copy('p5kvrm')
    password.send_keys(Keys.CONTROL,'v')
    login_botton = driver.find_element_by_id('log.login')
    login_botton.click()
except Exception as e:
    print(e)
finally:
    print('success')
"""
element = driver.find_element_by_id('query')
element.send_keys('컴퓨터')
element.send_keys(Keys.ENTER)
# element = driver.find_element_by_class_name('link_Login')
"""
elements = driver.find_elements_by_tag_name('a')
elements[0].get_attribute('href')
for idx,e in enumerate(elements):
    print(e.get_attribute('href'))
"""
time.sleep(1)
element.click()
time.sleep(1)
driver.back()
driver.forward()
driver.refresh()
driver.back()
"""