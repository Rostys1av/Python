from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://testdemy.com/")

driver.quit()