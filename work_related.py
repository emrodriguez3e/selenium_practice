import sys
import time
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


driver = webdriver.Safari()
driver.get('https://secure.rec1.com/account/login')
driver.implicitly_wait(10)
driver.find_element(By.TAG_NAME, 'input').send_keys('erodriguez@cypressca.org'+Keys.ENTER)
time.sleep(1)
clickable = driver.find_element(By.TAG_NAME, 'button')
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'form-control')



driver.quit()



