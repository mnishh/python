from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_run():
    browser = webdriver.Chrome()
    browser.get('http://www.Google.com')
    browser.quit()




