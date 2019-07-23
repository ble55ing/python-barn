#-*- coding: utf-8 -*-

import time
import datetime
import requests
import json
import re
import random
import code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

post = {}

debug=0
class XueXiQiangGuo:
    def __init__(self, NewsNum, NewsTime):
        self.NewsNum = NewsNum
        self.NewsTime = NewsTime
        self.dr = webdriver.Chrome(executable_path=r"C:\Users\hpwyyagi\AppData\Local\Google\Chrome\Application\chromedriver.exe")

    def login(self):
        self.dr.get("https://pc.xuexi.cn/points/login.html")
        ##Iframe = self.dr.find_elements_by_tag_name('iframe')[2]
        ##self.dr.switch_to.frame(Iframe)
        # QrData = self.dr.find_element_by_css_selector(".login_content>.login_body>.login_qrcode>.login_qrcode_content>img").get_attribute("src")
        ##QrData = self.dr.find_element_by_css_selector(".login_qrcode_content>img").get_attribute("src")
        # print QrData
        # QrStr = b64.b64decode(QrData.split(",")[-1])
        # QrImg = Image.frombytes(QrStr)
        # QrImg.show()
        ##self.dr.switch_to.default_content()
        raw_input()

    def learn(self):
        #self.dr.get("https://www.xuexi.cn/3695ce40a2f38ca24261ee28953ce822/9a3668c13f6e303932b5e0e100fc248b.html")
        #link = self.dr.find_elements_by_id("Ca4gvo4bwg7400")
        self.dr.get("https://www.xuexi.cn")
        time.sleep(5)
        if debug==0:
            time.sleep(10 + random.randint(0, 9))
        link = self.dr.find_elements_by_xpath("//span[@class='text']")
        #print link
        print "学习新闻:"
        time.sleep(5+random.randint(0,9))
        if debug==0:
            time.sleep(10 + random.randint(0, 9))
        start = random.randint(0,4)*(len(link)-20)/10
        print start
        MainPage = self.dr.current_window_handle
        for i in range(start,start+self.NewsNum):
            print link[i].text
            if u"精神" in link[i].text:
                return
            link[i].click()
            time.sleep(5+random.randint(2,5))
            if debug == 0:
                time.sleep(10 + random.randint(0, 9))
            AllPage = self.dr.window_handles
            ik=-1;
            for k in AllPage:
                ik+=1
                if ik==i+1-start:
                    self.dr.switch_to_window(k)
                    self.dr.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')
                    time.sleep(5 + random.randint(2, 10))
                    if debug == 0:
                        time.sleep(10 + random.randint(0, 9))
            #time.sleep(1)
            self.dr.switch_to_window(MainPage)
            time.sleep(5 + random.randint(5,8))
            if debug == 0:
                time.sleep(10 + random.randint(0, 9))

        MainPage = self.dr.current_window_handle
        AllPage = self.dr.window_handles
        print AllPage
        # LearnPage = {}
        print "-----"

        for i in AllPage:
            if i != MainPage:
                self.dr.switch_to_window(i)
                #self.dr.find_element_by_xpath("//div[@class='main-view']").send_keys(Keys.SPACE)

                # LearnPage[i] = self.dr.execute_script('return document.body.scrollHeight')
                self.dr.execute_script('window.scrollTo(0, document.body.scrollHeight/2)')
                time.sleep(5+random.randint(2, 5))
                if debug == 0:
                    time.sleep(10 + random.randint(0, 9))
        time.sleep(self.NewsTime*30+random.randint(5,30))

    def watch(self):
        # self.dr.get("https://www.xuexi.cn/3695ce40a2f38ca24261ee28953ce822/9a3668c13f6e303932b5e0e100fc248b.html")
        # link = self.dr.find_elements_by_id("Ca4gvo4bwg7400")
        self.dr.get("https://www.xuexi.cn")
        self.dr.maximize_window()
        time.sleep(5)
        if debug==0:
            time.sleep(10 + random.randint(0, 9))
        link = self.dr.find_elements_by_xpath("//div[@class='singleBox']")
        print link
        print len(link)
        linkleft = self.dr.find_elements_by_xpath("//div[@class='tab-wrapper horizontal-item']")
        MainPage = self.dr.current_window_handle
        print linkleft[11].text
        linkleft[11].click()
        k=11
        for i in range(0,16):
            self.dr.switch_to_window(MainPage)
            AllPage = self.dr.window_handles
            time.sleep(3)
            ik = -1;

            if i%3==0 :
                for j in AllPage:
                    if j != MainPage:
                        self.dr.switch_to_window(j)
                        self.dr.close()
                        time.sleep(1)
                time.sleep(5)
                if debug == 0:
                    time.sleep(10 + random.randint(0, 9))
            if i%4 ==0 and i!=0:
                self.dr.switch_to_window(MainPage)
                print linkleft[k].text
                linkleft[k].click()
                k+=1
                time.sleep(5)
                if debug == 0:
                    time.sleep(10 + random.randint(0, 9))
                link = self.dr.find_elements_by_xpath("//div[@class='singleBox']")
            self.dr.switch_to_window(MainPage)
            print link[i%4].text
            link[i%4].click()
            time.sleep(5)
            if debug == 0:
                time.sleep(10 + random.randint(0, 9))
            ik = -1;
            AllPage = self.dr.window_handles
            for j in AllPage:
                ik += 1
                if ik == i%4 + 1:
                    self.dr.switch_to_window(j)
                    self.dr.execute_script('window.scrollTo(0, document.body.scrollHeight/)')
                    time.sleep(5 + random.randint(2, 10))
                    if debug == 0:
                        time.sleep(10 + random.randint(0, 9))
                    break;



        #interp.interact("")
    def quit(self):
        self.dr.quit()

if __name__ == "__main__":
    interp = code.InteractiveConsole(globals())
    # 每次打开8篇文章,打开1分钟
    zz = XueXiQiangGuo(10,1)
    zz.login()
    zz.learn()
    #zz.watch()
    zz.quit()
