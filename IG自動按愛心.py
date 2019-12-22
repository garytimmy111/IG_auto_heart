# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:18:55 2019

@author: Ivan
"""
# selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import random
import time
import platform

#開啟selenium的driver
def open_driver():
    # 判斷是甚麼作業系統，決定selenium使用的工具
    theOS = list(platform.uname())[0]
    if theOS == 'Windows':
        theOS = theOS + '\\'
    else:
        theOS = theOS + '/'
    
    # 設定基本參數
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    #此處必須換成自己電腦的User-Agent
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    
    # PhantomJS driver 路徑 似乎只能絕對路徑
    driver = webdriver.PhantomJS(executable_path = theOS +'phantomjs', desired_capabilities=desired_capabilities)
    
    # 關閉通知提醒
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    
    # 開啟瀏覽器
    driver = webdriver.Chrome(theOS +'chromedriver',chrome_options=chrome_options)
    
    return driver

#登入  
def login(IGID = '您的IG帳號', IGpassword = '您的IG密碼', FBID = '您的FB帳號', FBpassword = '您的FB密碼' ):
    driver = open_driver()
    ####### 開始操作 輸入帳號密碼登入 到IG首頁 ####### 
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    assert "Instagram" in driver.title
    driver.find_elements_by_xpath("//*[contains(text(), '登入')]")[1].click() #點選登入
    driver.find_element_by_xpath('//*[@name="username"]').send_keys(IGID) #輸入登入帳號
    driver.find_element_by_xpath('//*[@name="password"]').send_keys(IGpassword) # 輸入登入密碼
    driver.find_elements_by_xpath("//*[contains(text(), '登入')]")[2].click() #按下登入按鈕
    time.sleep(5)
    
    if "Facebook" in driver.title:
        driver.find_element_by_id("email").send_keys(FBID)
        driver.find_element_by_id("pass").send_keys(FBpassword)
        driver.find_element_by_xpath('//*[@name="login"]').click() #按下登入按鈕
        time.sleep(5)
    return driver


class startSelenium:

    def __init__(self, IGID = '您的IG帳號', IGpassword = '您的IG密碼', FBID = '您的FB帳號', FBpassword = '您的FB密碼' ):
        self.IGID = IGID
        self.IGpassword = IGpassword
        self.driver = login(self.IGID, self.IGpassword, self.FBID, self.FBpassword)
        
    def checkShareGroup(self):
        print('======================== 即將發送的社團 ========================')
        for group in self.getallgroup:
            print(group)
            
class autoBot(startSelenium):
    
    def __init__(self, IGID, IGpassword, tags = 'love heart'):
        super().__init__(IGID, IGpassword)
        self.tags = tags.split(' ')
        
    def brown(self):
        ####### 模仿真人瀏覽行為，避免被封鎖 #######
        self.driver.get("https://www.instagram.com/")
        for i in range(1,random.randint(3,5)):
            for j in range(random.randint(1,5)):
                self.driver.find_elements_by_class_name('_9AhH0')[random.randint(1*i,9*i)].click() #隨便點選圖片
                time.sleep(random.randint(3,10))
                self.driver.find_element_by_xpath("//*[contains(text(), '關閉')]").click()
                time.sleep(random.randint(3,5))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(3,5))
    
    def clickHeart(self):
        ####### 開始操作 到不同的tag去發文 ####### 
        for tag in self.tags:
            self.driver.get("https://www.instagram.com/explore/tags/" + tag) #切換到該tag
            time.sleep(random.randint(2,5))
            self.driver.find_elements_by_class_name('_9AhH0')[9].click() #點選圖片(選擇最新發的)
            for i in range(random.randint(40,50)):
                if i % 10 == 1:
                    time.sleep(random.randint(5,20))
                try:
                    self.driver.find_element_by_xpath('//*[@aria-label="讚"]').click()
                except:
                    print('按過了')
                self.driver.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
                time.sleep(random.randint(1,5))
                
            print(tag +' 按完了')
            time.sleep(random.randint(7,15)) # 按完一個tag稍微休息一下，盡量模仿真人
            self.brown()
            
def main():         
    
    autoheart = autoBot(
            IGID='您的IG帳號',
            IGpassword = '您的IG密碼',
            FBID='您的FB帳號',
            FBpassword = '您的FB密碼',
            tags = 'guitar music')
    autoheart.clickHeart()
    

    
    
    
if __name__ == '__main__':
    main()