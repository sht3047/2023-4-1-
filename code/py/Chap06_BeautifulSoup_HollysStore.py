#========#========#========#========#
# write 
# 	230330
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 4주차
# 	- BeautifulSoup 사용하기 - Hollys 매장 탐색
#========#========#========#========#

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

for page in range(1,59):
    Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
    print(Hollys_url)
    html = urllib.request.urlopen(Hollys_url)
    # parsing html
    soupHhollys = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupHhollys.find('tbody')
    # get tag
    for store in tag_tbody.find_all('tr'):
        if len(store) <= 3:
            break
        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address = store_td[3].string
        store_phone = store_td[5].string
        result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    # Check the contents of store_td
    # len(result)
    # result[0]
    
    # store_td
    store_td[1].string
    store_td[0].string
    store_td[3].string
    store_td[5].string
    
    # save data csv
    hollys_tb1 = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
    hollys_tb1.to_csv("./chap06_data/hollys.csv", encoding= "cp949", mode= "w", index= True)
    print("[Magpie]:: Create hollys.csv")
    