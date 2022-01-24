import requests
import bs4
import pandas as pd
max_page = 2
col_len = 9
max_contents = 10
page_info = []
column_temp = ''
for page in range(1,max_page+1):
    url = f'http://www.cgs.or.kr/business/esg_tab04.jsp?pg={page}&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents'
    res = requests.get(url) # data call
    html_str = res.text # write
    bs_obj = bs4.BeautifulSoup(html_str) # using bs4 for tag search (data parsing)
    data = bs_obj.find_all(['th','tr'])
    if page == max_page:
        column_temp += data[0].get_text()
        column_idx = column_temp.split('\n')[1:1+col_len]
    temp = []
    for i in data[1+col_len:1+col_len+max_contents]:
        temp.append(i.get_text().split('\n'))
    for i in temp:
        page_info.append(i[1:1+col_len])
pandas_data = []
for i in range(eval(page_info[0][0])):
    pandas_data.append(page_info[i])
pandas_data.reverse()
df = pd.DataFrame(data=pandas_data,columns=column_idx)
print(df)






import requests
import bs4
import pandas as pd
max_page = 2
col_len = 9
max_contents = 10
page_info = []
for page in range(1,max_page+1):
    url = f'http://www.cgs.or.kr/business/esg_tab04.jsp?pg={page}&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents'
    res = requests.get(url) # data call
    html_str = res.text # write
    bs_obj = bs4.BeautifulSoup(html_str) # using bs4 for tag search (data parsing)
    data = bs_obj.find('div',{'class':'business_board'})
    th = data.find_all('th')
    td = data.find_all('td')
    if page == 1:
        columns = []
        for i in th:
            columns.append(i.get_text())
    contents = []
    contents_len = int(td[0].get_text())
    temp = []
    for i in td:
        if len(temp) == col_len:
            contents.append(temp)
            temp = [i.get_text()]
        else:
            temp.append(i.get_text())
    contents.append(temp)
    page_info.append(contents)
pandas_data = []
for i in page_info:
    for j in i:
        pandas_data.append(j)
pandas_data.reverse()
df = pd.DataFrame(data=pandas_data,columns=columns).set_index('NO')
print(df)
