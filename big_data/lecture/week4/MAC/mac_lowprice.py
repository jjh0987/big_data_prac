import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
from webdriver_manager.chrome import ChromeDriverManager
# test url
dep_loc = 'PUS'
arr_loc = 'SEL'
dep_date = 20220128
arr_data = 20220129
adult = 1
arr_loc_category = 'domestic' # domestic or international
child = 1
infant = 0
fare_type = 'YC' # YC:일반 ,P:프리미엄 ,C:비지니스 ,F:일등석


# 가장 저렴한 항공권 찾기
url = f"https://m-flight.naver.com/flights/{arr_loc_category}/" \
      f"{dep_loc}-{arr_loc}-{dep_date}/{arr_loc}-{dep_loc}-{arr_data}" \
      f"?adult={adult}&child={child}&infant={infant}&fareType={fare_type}"
# driver = webdriver.Chrome("/Users/junho/Desktop/main/big_data/lecture/week4/MAC/chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
WebDriverWait(driver, 50).until(
        EC.visibility_of_all_elements_located((By.XPATH ,'//*[@id="__next"]/div/div[1]/div[3]/div/div[3]/div')))
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# time.sleep(10)
lowprice_search_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/button')
lowprice_search_btn.click()
lowprice_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[1]/div/div/div/button[1]')
lowprice_btn.click()
lowprice = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')
lowprice.click()

src = driver.find_elements_by_class_name('SelectedFlight_summary__1t3j9')
for i in src:
    print(i.text)

bs_obj = bs4.BeautifulSoup(driver.page_source)
data = bs_obj.find_all('i',{'class':'num'})
print(data[0].text)

