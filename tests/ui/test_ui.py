import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait

# @pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service("/Users/sofindersky/Desktop/Automation-Course/qa-course" + "chromedriver"))

    #open https://github.com/login page
    driver.get("https://github.com/login")


    #Login field
    login_element = driver.find_element(By.ID, "login_field")


    #Fill in the field with incorrect data
    login_element.send_keys(" ")

    #Password field
    password_element = driver.find_element(By.ID, "password")


    #Fill in the password field with incorrect data
    #Fill in the field with incorrect data
    password_element.send_keys(" ")


    #Find the button 'sign in'
    button_element = driver.find_element(By.NAME, "commit")

    #Emulate the button click
    button_element.click()
    # time.sleep(2)

    # wait = WebDriverWait(driver, 5)

    #Verify the error message is shown
    # element_error = driver.find_element(By.XPATH, '//*[@id="js-flash-container"]/div')

    h1_header = driver.find_element(By.XPATH, '//*[@id="login"]/div[1]/h1')
    assert h1_header == 'Sign in to GitHub'
     #Close the browser
    driver.close()