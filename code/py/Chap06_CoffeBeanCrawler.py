#========#========#========#========#
# write 
# 	230330
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 4주차
# 	- selenium으로 동적 웹페이지 크롤링
#========#========#========#========#

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

# [CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_Url = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome('./chromedriver.exe')
    # wd = webdriver.Chrome('chromedriver', options=options)
    
    for i in range(1,50):
        print('[Magpie]:: for i = %d' %i)
        wd.get(CoffeeBean_Url)
        time.sleep(1)
        try:
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(1)
            html = wd.page_source
            
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            print('[Magpie]:: %s' %([store_name] + [store_address] + [store_phone]))
            result.append([store_name] + [store_address] + [store_phone])
            
        except:
            continue
        
    return



# [CODE 0]
def main():
    result = []
    print('[Magpie]:: CoffeeBean Store crawling')
    CoffeeBean_store(result)    # [CODE 1]

    CB_tb1 = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tb1.to_csv('./CoffeeBean_utf8.csv', encoding='utf-8', mode='w', index= True)
    print('[Magpie]:: Create File  |  ./CoffeeBean_utf8.csv')

if __name__ == '__main__':
    main()
