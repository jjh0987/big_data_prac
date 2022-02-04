import pandas as pd
import pymysql

table = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
temp = []
for i in range(len(table[0])):
    temp.append(list(table[0].iloc[i,:]))

con, cur = None, None
data1, data2 = "", ""
row = None

conn = pymysql.connect(host='localhost', user='root', password='jeon369!'
                       ,db='INVESTAR', charset='utf8')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS company_info (company char(20), code char(6))")

cur.execute('ALTER DATABASE investar CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;')
cur.execute('ALTER TABLE company_info CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')

for i in range(len(temp)):
    cur.execute(f'insert into company_info values'
                f'({temp[i][0]},{temp[i][1]});')

conn.commit()
conn.close()
