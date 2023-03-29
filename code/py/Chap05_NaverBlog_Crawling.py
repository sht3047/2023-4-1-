#========#========#========#========#
# write 
# 	230323
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 3주차
# 	- python과 네이버api를 이용한 크롤링 - Blog
#========#========#========#========#

import os
import sys
import urllib.request
import datetime
import time
import json

client_id = 'Sg5rTWjqcT4J0qWdCcZK'
client_secret = 'ar3Jc4Mav7'

# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url) #[CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

# [CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    link = post['link']
    description = post['description']
    blogger = post['bloggername']
    pDate = post['postdate']

    jsonResult.append({'blogger':blogger, 'cnt':cnt, 'description':description,'link':link, 'pDate':pDate, 'title': title})

    return

# [CODE 0]

def main():
    node = 'blog'
#     srcText = input('검색을 입력하세요 : ')
    srcText = '부산맛집'
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)    #[CODE 2]
    total = jsonResponse['total']
    print('total')
    print(total)

    print('jsonResult')
    print(jsonResult)

    while((jsonResponse != None) and (jsonResponse['display'] != 0)):
        if cnt == 100:
            break
        
        for post in jsonResponse['items']:
            cnt += 1

            print('jsonResult item')
            print(jsonResponse['items'])

            getPostData(post, jsonResult, cnt)    #[CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)    #[CODE 2]

    print('전체 검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False)
        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))
    

if __name__ == '__main__':
    main()

