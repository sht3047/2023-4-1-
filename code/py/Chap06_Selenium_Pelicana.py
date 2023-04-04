#========#========#========#========#
# write 
# 	230330
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 4주차
# 	- selenium으로 동적 웹페이지 크롤링 - Pelicana
#========#========#========#========#

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# [CODE 1]
def Pelicana_store(result):
    Pelicana_Url = "https://pelicana.co.kr/store/stroe_search.html?page="
    parameter = "&branch_name=&gu=&si="
    # [Window]
    wd = webdriver.Chrome('./chromedriver.exe')
    # [Linux]
    # wd = webdriver.Chrome('chromedriver', options=options)
    
    for i in range(1,6):
        url = Pelicana_Url + str(i) + parameter 
        wd.get(url)
        print('[Magpie]:: Create Url + Parameter')
        print(url)
        print()
        time.sleep(2)
        
        
        try:
            for row in range(1,11):
                selector = '#contents > table > tbody > tr:nth-child('+str(row)+') > td:nth-child(4) > a'
                
                wd.find_element(By.CSS_SELECTOR, selector).click()
                
                time.sleep(2)
                print('[Magpie]:: Search Element')
                html = wd.page_source
                soupP = BeautifulSoup(html, 'html.parser')
                
                branch_name_tag = soupP.select('#branch_name')
                branch_address_tag = soupP.select('#branch_address')
                branch_phone_tag = soupP.select('#branch_phone')  
                
                branch_name = branch_name_tag[0].string
                branch_address = branch_address_tag[0].string
                branch_phone = branch_phone_tag[0].string
                print('[Magpie]:: Result >>> %s' %([branch_name] + [branch_address] + [branch_phone]))
                result.append([branch_name] + [branch_address] + [branch_phone])
                wd.find_element(By.CSS_SELECTOR, '#popStore > div > p > a').click()
                time.sleep(2)
        except:
            print('[Magpie]:: Exception!')
            continue
        print()
    return


# [CODE 0]
def main():
    result = []
    print('[Magpie]:: Pelicana Store crawling')
    Pelicana_store(result)    # [CODE 1]

    PC_tb1 = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    PC_tb1.to_csv('./Pelicana_utf8.csv', encoding='utf-8', mode='w', index= True)
    print('[Magpie]:: Create File  |  ./Pelicana_utf8.csv')

if __name__ == '__main__':
    main()
