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
        sleep(3)
        self.page = self.driver.page_source
        self.soup = BeautifulSoup(self.page, 'lxml')
        
    def grab(self):
        self.val_grab = self.soup.find('li', class_='cn__listitem')
        print('\n\n######################\n\n\n')
        print(self.val_grab)
        
    def send(self, reciever, message):
        user = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(reciever))
        user.click()
        sleep(5)
        
        msg_box = self.driver.find_element_by_xpath('//div[@class="_2A8P4"]')
        msg_box.click()
        msg_box.send_keys('{}'.format(message))
        msg_box.click()
        msg_box.click()
        
        sleep(5)
        
        send_btn = self.driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
        send_btn.click()
        

bot = face_bot()

# bot.send("mad gir", "ok")

# bot.goto("https://www.bing.com/search?q=reading+whatspp+message+using+selenium&qs=n&form=QBRE&sp=-1&pq=reading+whatspp+m&sc=0-17&sk=&cvid=EA4136B7DA894C88AED1886A4D4D4A14")

bot.goto("https://edition.cnn.com/")

bot.getCode()
bot.grab()

bot.goto('https://web.whatsapp.com/')
bot.send('Moi Orange', bot.val_grab.text)
