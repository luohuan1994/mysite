# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://www.v2ex.com/signin"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

header = { "User-Agent": UA,
           "referer" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

}

v2ex_session = requests.Session()
f=v2ex_session.get(url,headers=header)

soup = BeautifulSoup(f.content,"html.parser")
once = soup.find('input',{'name':'once'})['value']
print(once)

postData = {
    'u':'840717800@qq.com',
    'p':'a7893482',
    'once':once,
    'next':'/'
}
v2ex_session.post(url,
                  data=postData,
                  headers=header)
f=v2ex_session.get('http://www.v2ex.com/settings',headers=header)
print(f.content.decode())