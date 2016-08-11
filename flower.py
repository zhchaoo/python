#!/usr/bin/python 
# coding: utf-8

import urllib,urllib2,cookielib,json,sys,time

username = "zhouchao"
password = "********"
people = {
            "黄耀悦",
            "陈剑光",
            "贺永明",
            "何建亮",
            "胡立琼",
            "谢学辉",
            "罗功武",
            "李海翔",
            "王晓振",
            "许国庆",
            "王永光",
            "曾锦和",
        }

outputKeys = {"id","name","description","text"}
collectedRes = {}
pointCount = 0
txtHeader = { 
            "Origin":"http://share.ucweb.local",
            "Referer":"http://share.ucweb.local/discuz/flower/flower.php",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5",
            }
url_login = "http://share.ucweb.local/discuz/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&inajax=1"
url_flush = "http://share.ucweb.local/discuz/flower/flower.php"
cookies = 0
comment = 0

# login share.ucweb.local
def login():
    global url_login,txtHeader,cookies,username,password
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    request = urllib2.Request(url_login, headers=txtHeader)

    para_dct = {}
    para_dct['fastloginfield'] = 'username'
    para_dct['username'] = username
    para_dct['password'] = password
    para_dct['quickforward'] = 'yes'
    para_dct['handlekey'] = 'ls'
    para_dct['questionid'] = '0'

    para_data = urllib.urlencode(para_dct)

    url = urlOpener.open(request, para_data)

    page = url.read(5000)

    cookies = filter(lambda h:isinstance(h, urllib2.HTTPCookieProcessor), urlOpener.handlers)[0].cookiejar

    print page, "!!!!", cookies ,"\n\n"

    return page

# flush flowers
def flushFlower():
    global url_flush,txtHeader,cookies,people,comment

    global url_login,txtHeader
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

    request = urllib2.Request(url_flush, headers=txtHeader)

    para_dct = {}
    para_dct['comment'] = comment

    for name in people:
        print "送花给", name, "中\n"

        para_dct['username'] = name

        para_data = urllib.urlencode(para_dct)

        url = urlOpener.open(request, para_data)

        page = url.read(5000)

        time.sleep(1)

        url.close()

# Main entry of the auto building tool
if __name__ =="__main__":
    print "请输入评论内容:"
    comment = sys.stdin.readline() 
    #1. send the request and data
    login()

    #2. convert JSON data to dictionary. 
    flushFlower()

