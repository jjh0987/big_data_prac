# 파이썬에서 쓰고 읽기
import pymysql
import csv
# f = open(r'../main/big_data/lecture/week5/data/data.csv','r',encoding='cp949')
# encoding='cp949' : default

# 전역변수 설정
conn, cur = None,None
data1,data2,data3,data4 = '','','',''
sql = ''

# main code
conn = pymysql.connect(host='localhost',user='root',password='jjh0987!',
                       db='mulcamDB',charset='utf8')
cur = conn.cursor()
# cur.execute('create database mulcamDB')
# workbench에서 작업
cur.execute('create table if not exists userTable '
            '(name char(3),sex char(1),department char(1),attendance char(1))')
f = open(r'../main/big_data/lecture/week5/data/data.csv','r',encoding='cp949')
data = csv.reader(f)
for i,row in enumerate(data):
    if i == 0:
        pass
    else:
        cur.execute(f'insert into userTable Values("{row[0]}","{row[1]}","{row[2]}","{row[3]}")')
f.close()
cur.execute('select * from userTable')
while 1:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print('%3s %1s %1s %1s' %(data1,data2,data3,data4))
conn.close()