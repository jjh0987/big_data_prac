import requests
import bs4
import pandas as pd
max_page = 2
business_head = []
business_body = []
for page in range(max_page,0,-1):
    url = f'http://www.cgs.or.kr/business/esg_tab04.jsp?pg={page}&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents'
    res = requests.get(url) # data call
    html_str = res.text # write
    bs_obj = bs4.BeautifulSoup(html_str,'html.parser') # using bs4 for tag search (data parsing)
    if page == 2:
        business_head.append(bs_obj.find_all('thead'))
    business_body.append(str(bs_obj.find('tbody'))) # search

head_list = str(business_head[0]).split('<th>')
column = []
for i in head_list:
    temp = ''
    for info in i:
        if info != '<':
            temp += info
        else:
            break
    if len(temp) != 0:
        column.append(temp)
column_idx = column[1:]

temp_body = []
for i in range(max_page):
    temp_body.append(str(business_body[i]).split('<tr>'))
temp_body.sort()
row = []
for page in temp_body: # page
    row_temp = []
    for strs in page: # str
        temp = ''
        for info in (strs.replace('</td>',',')).split('\n<td>'):
            if info != '<':
                temp += info
            else:
                break
        row_temp.append(temp)
    row.append(row_temp)

setting_row = []
numof_contents = 10
for page in range(max_page):
    for i in range(numof_contents+1):
        try:
            setting_row.append(row[page][i].split(','))
        except:
            break
pandas_data = []
for i in setting_row:
    if len(i) == 1:
        pass
    else:
        pandas_data.append(i[1:len(i[0])-2])
pandas_data.reverse()
df = pd.DataFrame(pandas_data,columns=column_idx[1:])
print(df)