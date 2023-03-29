#========#========#========#========#
# write 
# 	230330
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 3주차
# 	- 서울 열린데이터 광장 크롤링
#========#========#========#========#

import os
import sys
import urllib.request
import datetime
import time 
import json
import pandas as pd

# [Key]
ServiceKey = "" # Censored


# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    try:
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


# [CODE 2]
def getService(type, service, start_index, end_index, title):
    service_url = "http://openAPI.seoul.go.kr:8088/"
    
    # parameter = "/" + type + "/"
    # parameter += service + "/"
    # parameter += start_index + "/"
    # parameter += end_index + "/"
    # parameter += title
    
    parameter = "/%s/%s/%s/%s/%s" %(type, service, start_index, end_index, title)
    
    url = service_url + ServiceKey + parameter
    print("url")
    print(url)
    print("\n")

    responseDecode = getRequestUrl(url) # [CODE 1]
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

# [CODE 3]
def getPostData(count, post, result):
    sn = post['SN']
    title = post['TITLE']
    content = post['CONTENT']
    vote_score = post['VOTE_SCORE']
    reg_date = post['REG_DATE']
    
    
    result.append([count, sn, title, content, vote_score, reg_date])

    return

# [CODE 0]
def main():
    result = []
    
    print("<<<민주주의 서울 자유제안 정보>>>")
    type = "json"
    service = "ChunmanFreeSuggestions"
    start_index = 0
    end_index = 100
    print("[Magpie]:: 검색할 제목 키워드 (공란 가능) : ")
    title = ""
    count = 0

    # [CODE 2]
    jsonResponse = getService(type, service, start_index, end_index, title)
    # print(jsonResponse)
    total =jsonResponse['ChunmanFreeSuggestions']
    # print(total['row'])
    for post in total['row']:
        # print(post)
        count+=1
        # [CODE 3]
        getPostData(count, post, result)
    # print(result)
    # SAVE CSV FILE
    columns = ["Count", "제안번호", "제안제목", "제안내용(링크)", "득표수", "제안등록일"]
    result_csv = pd.DataFrame(result, columns= columns)
    result_csv.to_csv('./chap05_seoul.csv')
    print("[Magpie]:: Successed Create CSV File")

if __name__ == '__main__':
    main()