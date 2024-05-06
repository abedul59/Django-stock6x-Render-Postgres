a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://djinfo.cathaysec.com.tw/'
import random
my_Referer = random.choice([a,b,c,d])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

#stock_id = "2002"
'''
bankA = 'http://dj.mybank.com.tw/' #國泰世華
bankB = 'http://jdata.yuanta.com.tw/' #元大
bankC = 'http://jsjustweb.jihsun.com.tw' #日盛
bankD = 'http://stockchannel.sinotrade.com.tw' #永豐金證券
bankE = 'http://djfubonholdingfund.fbs.com.tw' #富邦證券

my_Banks = random.choice([bankA, bankB, bankC, bankD, bankE])
'''
import pandas as pd 
import requests
from bs4 import BeautifulSoup

def GetStockName(stock_id):  #由stock6改為stock6score 2020/5/7##計算六大指標平均 

    
####################取得股票名稱
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}

    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華 #不能隨便改 會發生錯誤 2020/10/22
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url + sheet_type + stock_id +'.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs[2][0][0][0:2]
    else:
        stock_name = dfs[2][0][0][0:3]
####################################
        
    #stock_description2 = '☆總大六大指標Mdj即時查詢評等☆' + '營益率指標為：' + st1 + '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 
     #+ stock_id_name + '。'
    #print(stock_description)
    return stock_name

