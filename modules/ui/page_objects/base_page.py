from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    PATH = r"/Users/sofindersky/Desktop/Automation-Course/qa-course/"
    DRIVER_NAME = "chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))


    def close(self):
        self.driver.close()    