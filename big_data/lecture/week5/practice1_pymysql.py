import pymysql

# 전역변수 설정
conn, cur = None,None
data1,data2,data3,data4 = '','','',''
sql = ''

# main code
conn = pymysql.connect(host='localhost',user='root',password='jjh0987!',
                       db='shoppingDB',charset='utf8')
cur = conn.cursor()
cur.execute('select * from userTable')
while 1:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print('%5s %15s %15s %d' %(data1,data2,data3,data4))

conn.close()