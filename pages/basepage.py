from pages import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
class BasePage(object):
    def __init__(self, driver, base_url='https://route-report.com'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)






