from django.shortcuts import render
from  bs4 import BeautifulSoup
from urllib.request import urlopen

# Create your views here.
def get_data(symbol):
    url = f'https://finance.naver.com/item/sise.nhn?code={symbol}'
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc,features='lxml',from_encoding='euc-kr')
        cur_price = soup.find('strong',id='_nowVal')
        cur_rate = soup.find('strong',id='_rate')
        stock = soup.find('title')
        stock_name = stock.text.split(':')[0].strip()
        return cur_price.text, cur_rate.text.strip(), stock_name
get_data('035420')

def main_view(request):
    # request : http://localhost:8000/balance/?035420=30&005930=100
    # urls.py :                       path   / request
    querydict = request.GET.copy() # ? input ? querydicd type : {'035420':['30']}
    mylist = querydict.lists() # ? 기업코드 [[기업코드,[주식수]],[code,[]]..]
    rows = []
    total = 0

    # mylist = [['035420',[100]],['005930',[30]]]

    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0])
        price = cur_price.replace(',','')
        stock_count = format(int(x[1][0]),',')
        sum = int(price)*int(x[1][0])
        stock_sum = format(sum,',')
        rows.append([stock_name,x[0],cur_price,stock_count
                     ,cur_rate,stock_sum])
        total = total + int(price) * int(x[1][0])

    total_amount = format(total,',')
    values = {'rows':rows,'total':total_amount}
    return render(request,'balance.html',values)

