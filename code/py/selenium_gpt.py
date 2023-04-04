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
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# [CODE 1]
def Pelicana_store(result):
    wd = webdriver.Chrome('./chromedriver.exe')
    wd.get("https://pelicana.co.kr/store/stroe_search.html?page=1&branch_name=&gu=&si=")
    time.sleep(3)

    # 테이블의 모든 tr 태그를 가져옴
    tbody = wd.find_element_by_xpath('//*[@id="contents"]/table/tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    
    for tr in trs:
        # tr 안의 a 태그를 가져와 클릭
        a_tag = tr.find_element_by_tag_name('a')
        wd.execute_script("arguments[0].click();", a_tag)
        time.sleep(2)
        
        # onclick이 실행되어 나타난 팝업창의 html 코드 가져오기
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        branch_name = soup.select('#branch_name')
        branch_address = soup.select('#branch_address')
        branch_phone = soup.select('#branch_phone')
        
        print('[Magpie]:: %s' %([branch_name] + [branch_address] + [branch_phone]))
        result.append([branch_name] + [branch_address] + [branch_phone])
        print()


# [CODE 0]
def main():
    result = []
    print('[Magpie]:: Pelicana Store crawling')
    Pelicana_store(result)    # [CODE 1]

    # PC_tb1 = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    # PC_tb1.to_csv('./Pelicana_utf8.csv', encoding='utf-8', mode='w', index= True)
    # print('[Magpie]:: Create File  |  ./Pelicana_utf8.csv')

if __name__ == '__main__':
    main()
