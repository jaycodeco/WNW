# import requests
from bs4 import BeautifulSoup

from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options


class face_bot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome Dev\\User Data\\Default')
        options.add_argument('--profile-directory=Default')
        
        self.driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome Dev\\Application\\chromedriver.exe', options=options)
        
    def goto(self, url):
        self.driver.get(url)
        sleep(5)
        
    def getCode(self):
        for i in range(0, 3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # print(i)
        sleep(3)
        self.page = self.driver.page_source
        self.soup = BeautifulSoup(self.page, 'lxml')
        
    def grab(self):
        self.val_grab = self.soup.find_all('h3', class_='cd__headline')
        print('\n\n######################\n\n\n')
        print(self.val_grab)
    
    def focus(self, contact):
        search = self.driver.find_element_by_xpath('//button[@class="_1Ek-U"]')
        search.click()
        sleep(2)
        
        # search_bar = self.driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
        search_bar = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_bar.click()
        search_bar.send_keys('{}'.format(contact))
        
        sleep(2)
        
        user = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
        user.click()
        sleep(5)
    
    def send(self,message):
        
        # msg_box = self.driver.find_element_by_xpath('//div[@class="_2A8P4"]')
        msg_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.click()
        msg_box.send_keys('{}'.format(message))
        msg_box.click()
        msg_box.click()
        
        sleep(5)
        
        send_btn = self.driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
        send_btn.click()
        


bot = face_bot()

bot.goto("https://edition.cnn.com/")

bot.getCode()
bot.grab()

news = bot.val_grab
bot.goto('https://web.whatsapp.com/')


bot.focus('Claud')
for info in news:
    bot.send(info.text)

bot.focus('Wiston')
for info in news:
    bot.send(info.text)

