#!/usr/bin/python

__author__ = 'ZhangJian'
import requests
import time
import sys
import os
import subprocess

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
'''
    login module
'''


class Index():
    def __init__(self, email, password):
        # declare global session
        self.session = requests.session()
        self.cookies = {}
        self.url = "http://www.zhihu.com/login/email"
        # construct headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'Host': 'www.zhihu.com',
            'Origin': 'http://www.zhihu.com',
            'Connection': 'keep-alive',
            'Referer': 'http://www.zhihu.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # construct data
        self.data = {
            "email": email,
            "password": password,
            "rememberme": "true"
        }

    def getXSRF(self):
        '''
        get xsrf
        :return:
        '''
        try:
            response = self.session.get("http://www.zhihu.com/#signin", headers=self.headers)
            # format html
            soup = BeautifulSoup(response.text.encode('utf-8'), "lxml")
            xsrf = str(soup.find_all("input")[0].get("value"))
        except:
            pass
        return xsrf

    def getCaptcha(self):
        '''
        get captcha
        :return:
        '''
        result = ""
        timsstamp = str(int(time.time() * 1000))
        captcha_URL = 'http://www.zhihu.com/captcha.gif?r=' + timsstamp
        captcha = self.session.get(url=captcha_URL, headers=self.headers)
        if not os.path.exists("captcha"):
            os.mkdir("captcha")
        # save captcha
        # @sys.path[0]
        try:
            with open("captcha/" + timsstamp + '.gif', 'wb') as f:
                f.writelines(captcha.content)
#            cmd = ["my_id=$(wmctrl -l -p | awk -v pid=$PPID '$3 == pid {print $1}')",
#                    "&", "display", sys.path[0] + "/captcha/" + timsstamp + ".gif",
#                    "&", "sleep", "0.1"
#                    ";", "wmctrl", "-i", "-a", '"$my_id"']
            cmd = ["display", sys.path[0] + "/captcha/" + timsstamp + ".gif", "&"]
            process = subprocess.Popen(cmd, shell=True)
            result = str(raw_input("[+]input captcha:"))
            process.kill()
        except:
            pass
        return result

    def login(self):
        '''
        post to login
        :return:
        '''
        self.data['_xsrf'] = self.getXSRF()
        self.data['captcha'] = self.getCaptcha()
        # print 'Test data:' + str(self.data)
        try:
            # post action
            p = self.session.post(url=self.url, data=self.data, headers=self.headers)
        except:
            pass
        req = self.session.get("http://www.zhihu.com/", headers=self.headers)
        self.cookies = self.session.cookies.get_dict()
        # windows8.1 handle encode
        return req.text.encode("gb18030")
        # windows xp handle encode
        # return req.text


# TEST
if __name__ == "__main__":
    i = Index('zhangjian12424@gmail.com', 'XXXX')
    i.login()
    r = requests.get(url='http://zhihu.com', cookies=i.cookies)
    print r.text.encode('gb18030')
