# 반응형 웹인 경우는 셀레니움 이용.
import pymysql
import requests
import bs4

# 전역변수 설정
conn, cur = None,None
data1,data2,data3 = '','',''
sql = ''

max_page = 2
page_toon = []
for page in range(1,max_page+1):
    url = f'https://comic.naver.com/webtoon/list?titleId=786537&page={page}'
    res = requests.get(url)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data_title = bs_obj.find_all('td',{'class':'title'})
    data_star = bs_obj.find_all('strong')
    data_date = bs_obj.find_all('td',{'class':'num'})
    for i in range(len(data_title)):
        temp = []
        temp.append(data_title[i].a.text)
        temp.append(data_star[i].text)
        temp.append(data_date[i].text)
        page_toon.append(temp)
page_toon.reverse()
page_toon

# main code
conn = pymysql.connect(host='localhost',user='root',password='jjh0987!',
                       db='crawStack',charset='utf8')
cur = conn.cursor()

# sql part
cur.execute('create table if not exists ComicBook'
            '(id int auto_increment primary key,'
            'subject char(30),'
            'star char(5),'
            'date char(10))')
for i in page_toon:
    cur.execute(f'insert into ComicBook(subject,star,date) Values("{i[0]}","{i[1]}","{i[2]}")')
cur.execute('select * from ComicBook')
while 1:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print('%d %30s %5s %10s' %(data1,data2,data3,data4))
conn.commit()
conn.close()

