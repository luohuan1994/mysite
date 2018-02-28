# -*- coding: UTF-8 -*-
import requests
import sys
import json
from bs4 import BeautifulSoup

s = requests.Session()

class JD:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer':'https://www.jd.com/'
        }

    def get_login_data(self):
        url = 'https://passport.jd.com/new/login.aspx'
        html = s.get(url,headers=self.headers).content
        soup = BeautifulSoup(html,'lxml')
        display = soup.select('#o-authcode')[0].get('style')
        auth_code = ''