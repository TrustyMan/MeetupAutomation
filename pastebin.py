from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import gmtime, strftime
import datetime
import time
import pandas
import re

# balance = {}
# profit = 0
url='http://pasted.co'
# mail_address = 'compactdev8877@gmail.com'
# mail_password = 'gmail8877'
# tags=('','ideas', 'components', 'technicals')


def wait_and_click(browser, path):
    WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, path))).click()

def wait_and_send_keys(browser, path, message):
    WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.XPATH, path))).send_keys(message)

def getBrowser():
    try:
        path_to_chromedriver = '/usr/lib/chromium-browser/chromedriver'
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=1200,1100')
        browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options=options)
        return browser
    except Exception as ex:
        print(ex)
        pass

def createMessageURL(browser, message):
    try:
        browser.get(url)
        browser.implicitly_wait(10)
        print('************************')
        print(message)
        print('************************')
        wait_and_send_keys(browser, '//*[@id="input_text"]', message)
        wait_and_click(browser, '//*[@id="main"]/form/div[2]/div/button')
        result = browser.find_element_by_xpath('//*[@class="input-copy"]/form/input[1]').get_attribute('value')
        # result = result[7:]
        time.sleep(5)
        print(browser.current_url)
        return result
    except Exception as ex:
        print(ex)
        pass

def closeBrowser(browser):
    try:
        browser.close()
    except Exception as ex:
        print(ex)
        browser.close()
        pass

# browser=getBrowser()
# message ="Hi, there"
# msg_url=createMessageURL(browser, message)
# closeBrowser(browser)
# print(msg_url)