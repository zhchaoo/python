#!/usr/bin/python 
# coding: utf-8

import urllib,urllib2,cookielib,json,sys,time,io,multiprocessing

outputKeys = {"id","name","description","text"}
pointCount = 0
txtHeader = { 
            "Origin":"http://blog.csdn.net",
            "Referer":"http://blog.csdn.net/zhchaoo",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5",
            }
url_portal = "http://blog.csdn.net/zhchaoo"
url_flush = "http://share.ucweb.local/discuz/flower/flower.php"
articleList = [] 
cookies = 0
comment = 0

# get blog article list.
def getPortalList():
    global url_portal,txtHeader,cookies,articleList
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    request = urllib2.Request(url_portal, headers=txtHeader)

    url = urlOpener.open(request)

    page = url.readlines()

    for line in page:
        if "link_title" in line:
            articleList.append(url_portal + line[50:-4])

    return page

# visitArticle
def visitArticle(link):
    global url_flush,txtHeader,cookies,people,comment

    global url_login,txtHeader
    urlOpener = urllib2.build_opener()

    request = urllib2.Request(link, headers=txtHeader)

    url = urlOpener.open(request)

    page = url.read()

    urlOpener.close()

# get articles
def getArticles():
    global url_flush,txtHeader,cookies,people,comment,articleList

    print "There are", len(articleList), "articles!"

    for link in articleList:
        print link

        visitArticle(link)

        time.sleep(1)

# get articles with multiprocessing
def getArticlesMutil():
    global url_flush,txtHeader,cookies,people,comment,articleList

    pool = multiprocessing.Pool(processes=4)

    result = []

    print "There are", len(articleList), "articles!"

    for link in articleList:
        print link

        result.append(pool.apply_async(visitArticle, (link, )))

    pool.close()

    pool.join()

#    for res in result:
#        print res.get()

    print "Sub-process(es) done."
        

# Main entry of the auto building tool
if __name__ =="__main__":
    #1. get csdn blog article list.
    getPortalList();

    #2. get articles.
    #getArticles();
    getArticlesMutil();

