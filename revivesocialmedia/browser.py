import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self, url):
        from chromedriver_py import binary_path # this will get you the path variable
        browser = webdriver.Chrome(executable_path=binary_path)
        browser.get(url)
        username = browser.find_element_by_id('username')
        username.send_keys(self.username)
        password = browser.find_element_by_id('password')
        password.send_keys(self.password)
        sign_in = browser.find_element_by_xpath("//button[@type='submit']")
        sign_in.click()
        time.sleep(5)
        try:
            allow = browser.find_element_by_id("oauth__auth-form__submit-btn")
            allow.click()
        except:
            pass
        return browser.current_url.split('?code=')[1].split('&state=')[0]
