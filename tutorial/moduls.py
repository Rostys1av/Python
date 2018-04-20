"""
importing other pieces of code
"""
#from selenium import webdriver
from webbrowser import open #import just one function
from webbrowser import * #import all functions
# import webbrowser
# webbrowser.open("http://google.com")

def open_youtube():
    open("http://youtube.com")

open_youtube()

def testdemy():
    driver = webdriver.Chrome()
    driver.get("http://testdemy.com")
    driver.close()
#testdemy()