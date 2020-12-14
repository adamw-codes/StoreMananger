from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv 
import credentials
import math
import random

class DepopManager():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def run(self):
        try:
            self.login()
            hashtags = self.getHashtags()
            self.refreshProduct()
            self.generateLikes(hashtags)
            self.driver.close()
            exit(0)
        except:
            self.driver.close()
            exit(0)

    def login(self):
        self.goToHomePage()
        time.sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="mainNavigation"]/li/a')
        login_btn.click()
        time.sleep(2)
        self.loginCredentials()
        time.sleep(2)
        loginlast_btn = self.driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]/form/button')
        loginlast_btn.click()
        time.sleep(2)
        close_btn = self.driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/button')
        close_btn.click()
    
    def refreshProduct(self):
        self.goToProfile()
        time.sleep(2)
        moveSoldItems_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[4]/div/button[1]')
        moveSoldItems_btn.click()
        time.sleep(2)
        self.scrollAll()
        totalProducts = self.getAvailProductsOnPage()
        soldProducts = self.getSoldProductsOnPage()
        availProducts = len(totalProducts) - len(soldProducts)
        self.goThroughProducts(availProducts, totalProducts, 0)

    def generateLikes(self, hashtags = []):
        self.goToSearchPage()
        time.sleep(2)
        self.scrollPage(24)
        exploreProducts = self.getAvailProductsOnPage()
        self.goThroughProducts(50, exploreProducts, 1)
        for x in range(len(hashtags)):
            self.goToSearchPage()
            time.sleep(2)
            search_bar = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/form/input')
            search_bar.click()
            time.sleep(2)
            search_bar.send_keys(hashtags[x])
            time.sleep(2)
            search_bar.send_keys(Keys.RETURN)
            time.sleep(2)
            self.scrollPage(12)
            searchProducts = self.getAvailProductsOnPage()
            self.goThroughProducts(25, searchProducts, 1)
            time.sleep(2)
    
    def goThroughProducts(self, length, set, action):
        for x in range(0, length, 1):
            if(action == 0):
                time.sleep(2)
                set[length-1].click()
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0, 200);")        
                edit_btn = self.driver.find_elements_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[3]/div/div[3]/div/a[1]')
                edit_btn[0].click()
                time.sleep(2)
                self.scrollAll()
                time.sleep(2)
                save_change = self.driver.find_elements_by_xpath('//*[@id="__next"]/div[2]/form/div[2]/button[1]')
                save_change[0].click()
                time.sleep(2)
                try:
                    save_change.click()
                except:
                    time.sleep(1)
                self.goToProfile()
                time.sleep(2)
                self.scrollAll()
                time.sleep(2)
                set = self.getAvailProductsOnPage()
            if(action == 1):
                time.sleep(2)
                self.scrollProducts(x)
                set[x].click()
                time.sleep(2)
                like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/div[2]/button')
                like_btn.click()
                time.sleep(2)
                self.driver.execute_script("window.history.go(-1)")
                time.sleep(2)
                set = self.getAvailProductsOnPage()
                
    def loginCredentials(self):
        username_btn = self.driver.find_element_by_xpath('//*[@id="username"]')
        username_btn.click()
        username_btn.send_keys(credentials.username)
        time.sleep(2)
        password_btn = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_btn.click()
        password_btn.send_keys(credentials.password)

    def getHashtags(self):
        hashtagBank = ["yellow", "blue", "cyan", "red", "black", "purple", "green", "white", "brown", "lime", "carhartt", "champion", "fubu", "bad religion", "nba", "film", "nyc", "michael jordan", "dallas", "kobe"]
        hashtags= []
        length = 19
        for x in range(0 , 5, 1):
            num = random.randint(0,length)
            hashtags.append(hashtagBank[num])
            hashtagBank.pop(num)
            length = length - 1
        return hashtags

    def goToProfile(self):
        time.sleep(2)
        profile_btn = self.driver.find_element_by_xpath('//*[@id="mainNavigation"]/li[4]/div/div')
        profile_btn.click()
        time.sleep(2)
        secProfile_btn = self.driver.find_element_by_xpath('//*[@id="userNavItem"]/a')
        secProfile_btn.click()
        time.sleep(2)
    
    def goToHomePage(self):
        self.driver.get('https://www.depop.com')

    def goToSearchPage(self):
        search_btn= self.driver.find_element_by_xpath('//*[@id="mainNavigation"]/li[1]/a')
        search_btn.click()
        
    def getAvailProductsOnPage(self):
        totalProductsList = self.driver.find_elements_by_css_selector("a[class^='styles__ProductCard']")
        return totalProductsList
        
    def getSoldProductsOnPage(self):
        soldProductsList = self.driver.find_elements_by_css_selector("div[class^='styles__SoldOverlay']")
        return soldProductsList

    def goToUserProfile(self):
        user_name = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/div/div[1]/div[1]/div[1]/div/p[1]/a')
        user_name.click()

    def goToFollowers(self):
        followers = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/button[1]/span[2]')
        followers.click()

    def getFollowersList(self):
        followersList = self.driver.find_elements_by_class_name("div[class^='styles__UserContainer']")
        return followersList

    def scrollPage(self, numOfProd):
        self.driver.execute_script("window.scrollTo(0, 160);")
        for x in range(0 , int(numOfProd/12), 1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    def scrollProducts(self, lines):
        if(lines < 12):
            self.driver.execute_script("window.scrollTo(0, 160);")
            time.sleep(2)
        if(lines >= 12 and lines < 24):
            self.driver.execute_script("window.scrollTo(0, 620);")
            time.sleep(2)
        if(lines >= 24 and lines < 36):
            self.driver.execute_script("window.scrollTo(0, 1100);")
            time.sleep(2)
        if(lines >= 36 and lines < 48):
            self.driver.execute_script("window.scrollTo(0, 1570);")
            time.sleep(2)
        if(lines >= 48 and lines < 60):
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(2)
        if(lines >= 60 and lines < 72):
            self.driver.execute_script("window.scrollTo(0, 2440);")
            time.sleep(2)
        if(lines >= 72 and lines < 84):
            self.driver.execute_script("window.scrollTo(0, 2920);")
            time.sleep(2)
        if(lines >= 84 and lines < 96):
            self.driver.execute_script("window.scrollTo(0, 3350);")
            time.sleep(2)
        if(lines >= 96 and lines < 108):
            self.driver.execute_script("window.scrollTo(0, 3820);")
            time.sleep(2)
        if(lines >= 108 and lines < 120):
            self.driver.execute_script("window.scrollTo(0, 4250);")
            time.sleep(2)

    def scrollAll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

bot = DepopManager()
bot.run()
