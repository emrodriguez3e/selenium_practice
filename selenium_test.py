import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service





ser = Service(executable_path="C:/Users/erodriguez/Documents/chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ser, options=op)


def google_search(search_input):
    driver.get('http://www.google.com')
    driver.implicitly_wait(2)
    text_box=driver.find_element(By.TAG_NAME, 'input')
    text_box.send_keys(search_input+Keys.ENTER)

    time.sleep(2)
    
    #clickable = driver.find_element(By.ID, 'footcnt')
    #ActionChains(driver).move_to_element(clickable).perform()

    scroll_origin = ScrollOrigin.from_element(text_box)
    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()


google_search('blue')
google_search('red')
google_search('yellow')

driver.quit()
