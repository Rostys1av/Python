import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()