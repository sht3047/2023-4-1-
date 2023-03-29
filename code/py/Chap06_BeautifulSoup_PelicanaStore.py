#========#========#========#========#
# write 
# 	230330
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 4주차
# 	- BeautifulSoup 사용하기 - Pelicana 매장 탐색
#========#========#========#========#

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

for page in range(1,106):
    pelicana_url = 'https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=' %page
    print(pelicana_url)
    html = urllib.request.urlopen(pelicana_url)
    
    # parsing html
    soupPelicana = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupPelicana.find('tbody')
    
    # get tag
    for store in tag_tbody.find_all('tr'):
        store_td = store.find_all('td')
        store_name = store_td[0].string
        store_address = store_td[1].string
        store_phone = store_td[2].string
        
        store_phone = str(store_phone)
        store_phone = store_phone.replace("\r\n\t\t\t\t\t\t\t\t", "")
        # print([store_name]+[store_address]+[store_phone])
        
        result.append([store_name]+[store_address]+[store_phone])
        
    # save data csv
    pelicana_tb1 = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    pelicana_tb1.to_csv("./chap06_data/pelicana.csv", encoding= "utf-8", mode= "w", index= True)
    print("[Magpie]:: Create pelicana.csv")