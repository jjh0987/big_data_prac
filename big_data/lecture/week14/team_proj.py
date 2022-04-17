import requests
import bs4

year_list = []
for year in range(2002, 2022 + 1):
    if year == 2022:
        url = 'https://www.federalreserve.gov/monetarypolicy/beige-book-default.htm'
    else:
        url = f'https://www.federalreserve.gov/monetarypolicy/beigebook{year}.htm'

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    article = soup.find('tbody') # {'class': 'col-xs-12 col-sm-8 col-md-8'}
    htmls = article.find_all('a')
    script = []

    i = 0
    for html in htmls:
        if '.htm' in html['href']:
            if year < 2017:
                if year > 2010:
                    sub_url = str(html['href']) + '?summary'
                    sub_res = requests.get(sub_url)
                    sub_html_str = sub_res.text
                    bs_obj = bs4.BeautifulSoup(sub_html_str)
                    data = bs_obj.find_all('div', {'id': 'div_summary'})[0]
                    script.append(data.text
                                  .replace('\n', ' ')
                                  .replace('\r', ' ')
                                  .replace('\t', ' ')
                                  .replace('\xa0', ' ')
                                  )
                    print(sub_url)
                else:
                    sub_url = str(html['href']) + '?summary'
                    sub_res = requests.get(sub_url)
                    sub_html_str = sub_res.text
                    bs_obj = bs4.BeautifulSoup(sub_html_str)
                    data = bs_obj.find_all('td')[4]
                    script.append(data.text
                                  .replace('\n', ' ')
                                  .replace('\r', ' ')
                                  .replace('\t', ' ')
                                  .replace('\xa0', ' ')
                                  )
                    print(sub_url)
            else:
                sub_url = 'https://www.federalreserve.gov'+str(html['href'])[:31] + '-summary.htm'
                sub_res = requests.get(sub_url)
                sub_html_str = sub_res.text
                bs_obj = bs4.BeautifulSoup(sub_html_str)
                data = bs_obj.find_all('div', {'id': 'article'})[0]
                script.append(data.text
                              .replace('\n',' ')
                              .replace('\r',' ')
                              .replace('\t',' ')
                              .replace('\xa0',' ')
                              )
                print(sub_url)

    print(year)
    year_list.append(script)

import pandas as pd
df = pd.DataFrame(data=year_list)

df.to_csv('')
df.iloc[0,0] # return to -->