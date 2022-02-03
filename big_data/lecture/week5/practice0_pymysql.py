import pymysql

# 전역변수 설정
conn, cur = None,None
sql = ''

# main code
conn = pymysql.connect(host='localhost',user='root',password='jjh0987!',
                       db='shoppingDB',charset='utf8')
cur = conn.cursor()

cur.execute('create table if not exists userTable '
            '(id char(4),userName char(15),email char(20),birthYear int)')
cur.execute('insert into userTable Values("jhon","jhon Bann","jhon@naver.com",1990)')
cur.execute('insert into userTable Values("kim","kim Bann","kim@naver.com",1991)')
cur.execute('insert into userTable Values("park","park Bann","park@naver.com",1992)')

conn.commit()
conn.close()