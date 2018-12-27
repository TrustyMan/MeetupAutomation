from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import gmtime, strftime
import datetime
import time
import pandas

# balance = {}
# profit = 0
login_url='https://secure.meetup.com/login/'
# mail_address = 'compactdev8877@gmail.com'
# mail_password = 'gmail8877'
# tags=('','ideas', 'components', 'technicals')


def wait_and_click(browser, path):
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, path))).click()

def wait_and_send_keys(browser, path, message):
    WebDriverWait(browser, 30).until(
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

def login(browser, mail_address, mail_password):
    try:
        sId = browser.session_id;
        browser.get(login_url)
        browser.implicitly_wait(3)
        wait_and_click(browser, '//*[@id="button-google"]')
        wait_and_send_keys(browser, '//*[@id="identifierId"]', mail_address)
        wait_and_click(browser, '//*[@id="identifierNext"]')
        wait_and_send_keys(browser, '//*[@id="password"]/div[1]/div/div/input', mail_password)
        wait_and_click(browser, '//*[@id="passwordNext"]')
        # wait_and_send_keys(browser, '//*[@id="email"]', mail_address)
        # wait_and_send_keys(browser, '//*[@id="password"]', mail_password)
        # wait_and_click(browser, '//*[@name="submitButton"]')
        # while(sId == browser.session_id):
        # time.sleep(60)
        # print(browser.session_id)
        # time.sleep(5)
        return browser.session_id
    except Exception as ex:
        print(ex)
        pass

def sendMessage(browser, url, message, sId):
    try:
        browser.get(url)
        browser.session_id = sId
        time.sleep(3)
        wait_and_click(browser, '//*[@class="j-composeNewMessage"]')
        wait_and_send_keys(browser, '//*[@id="messaging-new-convo"]', message)
        wait_and_click(browser, '//*[@id="messaging-new-send"]')
        # time.sleep(1000)
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

# browser = getBrowser()
# sId = login(browser)
# url = 'https://www.meetup.com/Newcomers-networking-Real-Estate-investment-professionals/members/?op=leaders'
# message = "Hi there, I’m reaching out see if I can create an opportunity to collaborate with you.My organization (Arcadia Group) is hosting a VIP event for potential real estate, blockchain, artificial intelligence and franchise investors and I would love to have an opportunity to invite your members. In exchange, I would love to promote your meetup events to our members. With over 20 years of business experience, I’ve discovered collaboration and working with others dramatically fast forwards each other’s objectives.We have over 11 meetup groups with over 600 members in all of them combined & I would love to contribute to your goals as well as ask for you to help promote our events to your members."

# sendMessage(browser, url, message, sId)
# print("xxxxxxxxx")
# browser.execute_script("window.history.go(-1)")
# print("xxxxxxxxx")