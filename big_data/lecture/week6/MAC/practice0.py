import pymysql,calendar,time,json
from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime
from threading import Timer

class DBupdate:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',
                                    password='jjh0987!',db='INVESTAR10',charset='utf8')
        with self.conn.cursor() as curs:
            sql = 'create table if not exists company_info(' \
                  'code varchar(20),' \
                  'company varchar(40),' \
                  'last_update DATE,' \
                  'primary key(code));'
            curs.execute(sql)
            sql = 'create table if not exists daily_price(' \
                  'code varchar(20),' \
                  'date date,' \
                  'open bigint,' \
                  'high bigint,' \
                  'low bigint,' \
                  'close bigint,' \
                  'diff bigint,' \
                  'volume bigint,' \
                  'primary key(code,date))'
            curs.execute(sql)
        self.conn.commit()
        self.codes = dict()

    def __del__(self):
        self.conn.close()

    # krx
    def read_krx_code(self):
        url = f'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
        krx = pd.read_html(url,header=0)[0]
        krx = krx[['종목코드','회사명']]
        krx = krx.rename(columns={'종목코드':'code','회사명':'company'})
        krx.code = krx.code.map('{:06f}'.format) # data가 float이라 에러 url 데이터 이상.
        krx
        return krx

    def update_krx_code(self):
        pass

    def update_comp_info(self):
        sql = 'select * from company_info'
        df = pd.read_sql(sql,self.conn)
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]] = df['company'].values[idx]

        with self.conn.cursor() as curs:
            sql = 'select max(last_update) from company_info'
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]

                    sql = f"replace into company_info(code,company,last_update) ' \
                          f'values('{code}','{company}','{today}');"
                    curs.execute(sql)
                    self.codes[code] = company # codes : dict

                    # logs
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f'[{tmnow}] #{idx+1:04d} : {sql}')

                self.conn.commit()

    # naver
    def read_naver(self,code,company,pages_to_fetch):
        try:
            df = pd.DataFrame()
            url = f'http://finance.naver.com/item/sise_day.nhn?code={code}'
            html = BeautifulSoup(requests.get(url,headers={'User-agent':'Mozilla/5.0'}).text,'lxml')
            pgrr = html.find('td',class_='pgrr')
            if pgrr is None:
                return None
            s = str(pgrr.a['herf']).split('=')
            last_page = s[-1]
            pages = min(int(last_page),pages_to_fetch)

            for page in range(1,pages+1):
                pg_url = f'{url}&page={page}'
                df = df.append(pd.read_html
                               (requests.get(pg_url,headers={'User-agent':'Mozilla/5.0'}).text)[0])

                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}],{},({}) : {:04d}/{:04d} loading..'.format(tmnow,company,code,page,pages),end='\r')

                df.rename(columns={'날짜':'date','종가':'closs','전일비':'diff','시가':'open','고가':'high'
                                   ,'저가':'low','거래량':'volume'})
                df['date'] = df['date'].replace('.','-')
                df = df.dropna()
                df[['close','diff','open','high','low','volumne']] = \
                    df[['close','diff','open','high','low','volumne']].astype(int)
                df = df[['date','open','high','low','close','diff','volume']]

        except Exception as e:
            print('Exception occured :',str(e))
            return None
        return df

    def replace_into_db(self,df,num,code,company):
        with self.conn.cursor() as curs:
            for r in df.itertuples():
                sql = f"replace into daily_price values ('{code}','{r.date}'," \
                      f"'{r.open}','{r.high}','{r.low}','{r.close}','{r.diff}','{r.volume}')"
                curs.execute(sql)
                self.conn.commit()

                print('[{}] #{:04d} {} ({}) : {} rows > replace into daily_price [OK]'
                      .format(datetime.now().strftime('%Y-%m-%d %H:%M'),num+1,company,code,len(df)))

    def update_daily_price(self,pages_to_fetch):
        # 네이버로부터 읽어서 db 업데이트
        for idx,code in enumerate(self.codes):
            if code != '263750':
                continue
            df = self.read_naver(code,self.codes[code],pages_to_fetch)
            if df is None:
                continue

        self.replace_into_db(df,idx,code,self.codes[code])

    def excute_daily(self):
        self.update_comp_info()

        try:
            with open('conffig.json','r') as in_file: # path
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        except FileExistsError:
            with open('config.json','w') as out_file: # path
                pages_to_fetch = 50
                config = {'pages_to_fetch':pages_to_fetch}
                json.dump(config,out_file)

        self.update_daily_price()

if __name__ == '__main__':
    dbu = DBupdate()
    dbu.read_krx_code()
