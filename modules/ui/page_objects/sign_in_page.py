from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init_(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password) :
        #Login field
        login_element = self.driver.find_element(By.ID, "login_field")


        #Fill in the field with incorrect data
        login_element.send_keys(username) 

            #Password field
        password_element = self.driver.find_element(By.ID, "password")


        #Fill in the password field with incorrect data
        #Fill in the field with incorrect data
        password_element.send_keys(password)


            #Find the button 'sign in'
        button_element = self.driver.find_element(By.NAME, "commit")

        #Emulate the button click
        button_element.click()


    def check_title(self, expected_title):
        return self.driver.title == expected_title   


