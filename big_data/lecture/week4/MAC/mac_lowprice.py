import time
from selenium import webdriver
import bs4

# test url
dep_loc = 'PUS'
arr_loc = 'SEL'
dep_date = 20220125
arr_data = 20220127
adult = 1
arr_loc_category = 'domestic' # domestic or international
child = 1
infant = 0
fare_type = 'YC' # YC:일반 ,P:프리미엄 ,C:비지니스 ,F:일등석


# 가장 저렴한 항공권 찾기
url = f"https://m-flight.naver.com/flights/{arr_loc_category}/" \
      f"{dep_loc}-{arr_loc}-{dep_date}/{arr_loc}-{dep_loc}-{arr_data}" \
      f"?adult={adult}&child={child}&infant={infant}&fareType={fare_type}"
driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/chromedriver")
driver.get(url)

time.sleep(10)
lowprice_search_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/button')
lowprice_search_btn.click()
lowprice_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/div/button[1]')
lowprice_btn.click()
lowprice = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')
lowprice.click()

print(driver.find_element_by_class_name('num').text)

bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('i',{'class':'num'})
print(data[0].text)