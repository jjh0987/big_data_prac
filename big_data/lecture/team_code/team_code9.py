import pymysql
import requests
import bs4
import time
import csv

class craw:
    def __init__(self,target_url):
        self.url = target_url

    def get_bs4(self):
        res = requests.get(self.url)
        html_str = res.text
        return bs4.BeautifulSoup(html_str, features='lxml')

    def get_bs4_headers(self,engine):
        headers = {'User-Agent': engine}
        res = requests.get(self.url, headers=headers)
        html_str = res.text
        return bs4.BeautifulSoup(html_str)

    def get_primary_key_data(self,pg_data,col_idx):
        primary_key = []
        for i in pg_data:
            primary_key.append(i[col_idx])
        return primary_key

class enter_sql:
    def __init__(self,host,user,password,db,charset): # class 인풋 변수
        self.conn = pymysql.connect(host=host,user=user,password=password,
                       db=db,charset=charset)
        self.cur = self.conn.cursor()

    def query_execute(self,query):
        self.cur.execute(query)

    def insert_execute(self,sql,parms):
        self.cur.execute(sql,parms)

    def setting_fk(self,origin_table,ref_table,ref_column):
        self.cur.execute(f'alter table {origin_table} add constraint foreign key({ref_column}) '
                         f'references {ref_table}({ref_column});')

    def exit_sql(self):
        self.conn.commit()
        self.conn.close()

    def encoding(self,db,table):
        self.cur.execute(f'ALTER DATABASE {db} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;')
        self.cur.execute(f'ALTER TABLE {table} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')

    def data_call(self,columns,table):
        column = ''
        for i in columns:
            column += i + ','
        column = column.strip(',')
        data = []
        self.cur.execute(f'select {column} from {table}')
        while 1:
            row = self.cur.fetchone()
            if row == None:
                break
            temp = []
            for i in range(len(columns)):
                temp.append(row[i])
            data.append(temp)
        for i in data:
            print(i)

    def select_data(self,columns,table):
        column = ''
        for i in columns:
            column += i + ','
        column = column.strip(',')
        self.cur.execute(f'select {column} from {table}')

    def fetch_data(self):
        self.cur.fetchone()
day = 0
while 1:
    if time.localtime()[3] == 17 and time.localtime()[4] == 0 and time.localtime()[5] == 0:
        day += 1
        # craw company info
        myCraw = craw(f'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
        bs_obj = myCraw.get_bs4()
        data_head = bs_obj.find_all('th')
        data = bs_obj.find_all('td')

        columns = [i.text for i in data_head]
        columns

        # caution column 7
        temp = []
        for i in data:
            temp.append(i.text)

        page_data = []
        temp = []
        target = ['\r','\n','\t']
        for i in data:
            if len(temp) == len(columns):
                page_data.append(temp)
                temp = []
            if len(temp) == 7:
                x = i.text
                for j in target:
                    x = x.replace(j,'')
                temp.append(x)
            else:
                temp.append(i.text)
        page_data[0]


        # company code
        primary_key = myCraw.get_primary_key_data(page_data,1)
        primary_key

        # craw price info
        price_info = []
        i = 1
        engine = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        for company_code in primary_key:
            url = 'http://finance.naver.com/item/sise_day.nhn?code='+company_code
            myCraw = craw(url)
            bs_obj = myCraw.get_bs4_headers(engine)
            data = bs_obj.find_all('span',{'class':'tah p11'})
            price_info.append(data[0].text)
            print(f'success load {i}/{len(primary_key)}')
            i += 1


        # sql

        mysql_mine = enter_sql('localhost','root','jjh0987!','INVESTAR1','utf8')
        mysql_mine.query_execute(f'create table if not exists company'
                    f'({columns[0]} char(25),'
                    f'{columns[1]} char(6) primary key,'
                    f'{columns[2]} char(50),'
                    f'{columns[3]} LONGTEXT,'
                    f'{columns[4]} char(10),'
                    f'{columns[5]} char(3),'
                    f'{columns[6]} LONGTEXT,'
                    f'{columns[7]} char(50),'
                    f'{columns[8]} char(10))')
        mysql_mine.encoding('INVESTAR1','company')
        sql = """replace into company values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        for i in page_data:
            mysql_mine.insert_execute(sql,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        mysql_mine.exit_sql()

        #
        mysql_mine = enter_sql('localhost','root','jjh0987!','INVESTAR1','utf8')

        mysql_mine.query_execute(f'create table if not exists price_info('
                    f'{columns[1]} char(6),'
                    f'today_price char(20))')
        mysql_mine.setting_fk('price_info','company','종목코드')
        mysql_mine.encoding('INVESTAR1','price_info')
        sql = """replace into price_info values (%s, %s);"""
        for i in range(len(primary_key)):
            mysql_mine.insert_execute(sql,(primary_key[i],price_info[i]))

        mysql_mine.exit_sql()
    if time.localtime()[5] == 0:
        time.sleep(1)
        print(time.localtime())
    if day == 100:
        break
#
mysql_mine = enter_sql('localhost','root','jjh0987!','INVESTAR1','utf8')
mysql_mine.data_call(['회사명','대표자명'],'company') # 조회만 가능하다.
mysql_mine.exit_sql()




'''
week = 0
    if day%7 == 0:
        week += 1
        mysql_mine = enter_sql('localhost', 'root', 'jjh0987!', 'INVESTAR1', 'utf8')

        f = open(f'../main/big_data/lecture/team_code/data/week{week}','w',newline='')
        write = csv.writer(f)
        mysql_mine.select_data(['회사명', '대표자명'], 'company')
        while 1:
            row = mysql_mine.fetch_data()
            if row == None:
                break
            temp = []
            for i in range(2):
                temp.append(row[i])
            f.write(temp)
        f.close()

        mysql_mine.exit_sql()
'''