from selenium import webdriver
from time import sleep
from login_details import email, password


class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/V/Desktop/chromedriver.exe')

    def login(self):
        self.driver.get('https://bumble.com/get-started')
        sleep(3)

        
        
        

        fb_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/button')
        fb_btn.click()
        sleep(4)
         #switch pages
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(4)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        sleep(2)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
        login_btn.click()
        sleep(4)
        self.driver.switch_to_window(base_window)
        sleep(15)
        
        
        like_btn = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')

        i=1
        while True:
            try:
                like_btn.click()

                sleep(2)
                print(f"Swiped right for {i} times")
                i += 1
            except:
                sleep(5)

           


bot = BumbleBot()
bot.login()



