import time
from selenium import webdriver
import bs4

# 가장 저렴한 항공권 찾기
url = 'https://m-flight.naver.com/'
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/MAC/chromedriver")
driver.get(url)

time.sleep(1)
departure_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]')
arrival_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]')
departure_date_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')
arrival_date_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[2]')
search_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button')

departure_btn.click()
departure_city = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input')
departure_city.click()
departure_city.send_keys('부산')
time.sleep(0.5)
select_city = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a')
select_city.click()

arrival_btn.click()
arrival_city = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input')
arrival_city.click()
arrival_city.send_keys('서울')
time.sleep(0.5)
select_city = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a[2]')
select_city.click()
time.sleep(0.5)

departure_date_btn.click()
time.sleep(0.5)
departure_date = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button')
departure_date.click()
time.sleep(0.5)
arrival_date = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button')
arrival_date.click()
time.sleep(0.5)

search_btn.click()
time.sleep(10)

# next page
lowprice_search_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/button')
lowprice_search_btn.click()
lowprice_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/div/button[1]')
lowprice_btn.click()
lowprice = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')
lowprice.click()

# data load
url = 'https://m-flight.naver.com/flights/domestic/PUS-SEL-20220125/SEL-PUS-20220127?adult=1&child=0&infant=0&fareType=YC&selectedFlight=LJ-362-202201252035-L'
driver.get(url)
bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('i',{'class':'num'})
print(data[0].text)