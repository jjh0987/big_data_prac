from selenium import webdriver
import bs4

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

driver.find_element_by_xpath('//*[@id="article"]/ul[2]/li[3]/a').click()

bs_obj = bs4.BeautifulSoup(driver.page_source)
target = bs_obj.find('div',{'class':'angularEvents items ng-scope'})
atag = target.find_all('a')
for a in atag:
    if '.htm' in a['href']:
        url = 'https://www.federalreserve.gov' + a['href']

# ref 타고 들어가기
# fin.