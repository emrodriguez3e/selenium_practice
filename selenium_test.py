#! /usr/bin/env python3
# Import stl
import sys

# Import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# Check system platform
if sys.platform == 'darwin':
    ser = Service(executable_path='/Users/enriquerodriguez/chromedriver')
elif sys.platform == 'win32':
    ser = Service(executable_path='C:/Users/erodriguez/Documents/chromedriver.exe')
else:
    print('Unable to find chrome driver')
    exit()

op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])


def safari_search(search_input):
    driver = webdriver.Safari()
    google_move(search_input, driver)


def google_search(search_input):
    driver = webdriver.Chrome(service=ser, options=op)
    google_move(search_input, driver)


def google_move(search_input, driver):
    driver.get('https://www.google.com')
    driver.implicitly_wait(2)
    text_box = driver.find_element(By.TAG_NAME, 'input')
    text_box.send_keys(search_input + Keys.ENTER)

    driver.implicitly_wait(5)

    text_box = driver.find_element(By.TAG_NAME, 'input')
    scroll_origin = ScrollOrigin.from_element(text_box)
    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()
    driver.quit()


safari_search('red')
safari_search('blue')
