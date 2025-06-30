from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class BumbleBot():
    def __init__(self):
        service = Service('C:/Users/DELL/Desktop/project/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get('https://bumble.com/get-started')
        sleep(3)

    
        security_key_btn = bot.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div/div/div[1]/div')
        security_key_btn.click()
        sleep(45)
         #switch pages
        #base_window = self.driver.window_handles[0]
        #self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(4)
                    
        like_btn = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')

        i=1
        while True:
            try:
                like_btn.click()

                sleep(1.2)
                print(f"Swiped right for {i} times")
                i += 1
            except:
                sleep(5)

           


bot = BumbleBot()
bot.login()


