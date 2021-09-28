from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import time


class InstagramBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(executable_path="./chromedriver")
  
    
    def WaitForObject(self, type, string):
        return WebDriverWait(self.browser,3).until(EC.presence_of_element_located((type, string)))

    def WaitForObjects(self, type, string):
        return WebDriverWait(self.browser,3).until(EC.presence_of_all_elements_located((type, string)))
    
    def login(self):
        self.browser.get("https://instagram.com/accounts/login")
        
        #login details area
        login_objects = self.WaitForObjects(By.CSS_SELECTOR,"input._2hvTZ.pexuQ.zyHYP")

        login_objects[0].send_keys(self.username)
        login_objects[1].send_keys(self.password)
        login_objects[1].send_keys(Keys.ENTER)
        sleep(5)
        
        #pre window 1
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)
        
        #pre window 2
        self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        sleep(2)
        
        #searching for hashtags
        
    def search_hashtags(self, hashtag):
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
        sleep(2)

        all_photos = self.WaitForObjects(By.CSS_SELECTOR,"div.v1Nh3.kIKUG._bz0w")
        sleep(2)

        #depends on your language you have to change the aria-label name
        for photo in all_photos:
            photo.click()
            self.WaitForObject(By.CSS_SELECTOR,"[aria-label='Gefällt mir']").click()
            self.WaitForObject(By.CSS_SELECTOR,"[aria-label='Schließen']").click()
            sleep(5)


Bot = InstagramBot("add here your username","here your password")

Bot.login()

Bot.search_hashtags("add here your hashtag")
