import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def main():
    # Check system platform
    if sys.platform == 'darwin':
        ser = Service(executable_path='/Users/enriquerodriguez/chromedriver')
    elif sys.platform == 'win32':
        ser = Service(executable_path='C:/Users/erodriguez/Documents/chromedriver.exe')
    else:
        print('Unable to find chrome driver')
        exit()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    safari_options = webdriver.WebKitGTKOptions()

    driver = webdriver.Safari()
    driver.get('https://secure.rec1.com/account/login')

    driver.find_element(By.TAG_NAME, 'input').send_keys('erodriguez@cypressca.org' + Keys.ENTER)
    time.sleep(1)
    clickable = driver.find_element(By.TAG_NAME, 'button')
    ActionChains(driver).click(clickable).perform()

    time.sleep(2)

    driver.find_element(By.NAME, 'Input.Email').send_keys('erodriguez@cypressca.org')
    driver.find_element(By.NAME, 'Input.Password').send_keys('Spac3Curv3!?' + Keys.ENTER)

    time.sleep(3)
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, "//*[contains(text(), '(6078)')]").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//li[4]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Permit')]").click()
    time.sleep(2)
    driver.find_element(By.ID, 'rec1-permit-editor-permit-number').send_keys('6488' + Keys.ENTER)
    driver.find_element(By.CLASS_NAME, 'btn btn-default rec1-permit-editor-view').click()

    print('Test successful')
    time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    main()
