#! /usr/bin/env python3
# Import stl
import sys
import time

# Import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Function to move around google search engine
def google_search(search_input, driver):
    # Set start page
    driver.get('https://www.google.com')
    driver.implicitly_wait(2)
    
    # Find search box
    text_box = driver.find_element(By.TAG_NAME, 'textarea')
    text_box.send_keys(search_input + Keys.ENTER)

    # Wait for the page to load
    driver.implicitly_wait(10)
    


# Choose which browser to use
def browser_choice(search_parameter):
    driver = None
    if sys.platform == 'darwin':
        driver = webdriver.Safar()
        
    elif sys.platform == 'win32' or sys.platform == 'linux':
        driver = webdriver.Chrome(service=ser, options=op)
        
    else:
        driver = webdriver.Firefox()
        
    
    # Start function
    google_search(search_parameter, driver)
    time.sleep(2)
    #driver.quit()


# Check system platform
if sys.platform == 'darwin':
    ser = Service(executable_path='/Users/enriquerodriguez/chromedriver')
elif sys.platform == 'win32':
    ser = Service(executable_path='C:/Users/erodriguez/Documents/chromedriver.exe')
elif sys.platform == 'linux':
    ser = Service(executable_path='chromedriver')
else:
    print('Unable to find chrome driver')
    exit()

op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])

browser_choice('red')
time.sleep(2)


