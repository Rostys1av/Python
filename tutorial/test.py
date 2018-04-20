import time
import unittest

from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.route-report.com")
        driver.maximize_window()
        self.assertIn("Route Report - Earn money while traveling", driver.title)
        elemBtnLogin = driver.find_element_by_id("open-login")
        elemBtnLogin.click()
        driver.implicitly_wait(50)
        elemMail = driver.find_element_by_id("in_login")
        elemMail.send_keys("rostyslav.biliaiev@route-report.com")
        elemPass = driver.find_element_by_id("in_password")
        elemPass.send_keys("111111")
        elemBtnLoginPopup = driver.find_element_by_xpath(".//*[@id='windowLogin1']/div[1]/div[5]/div[2]/button")
        time.sleep(5)
        elemBtnLoginPopup.click()
        time.sleep(5)
        driver.implicitly_wait(10)
        self.assertIn("Account - Report Report", driver.title)
        elemBtnEditReport = driver.find_element_by_xpath("(//i[@class='fa fa-pencil'])[1]")
        elemBtnEditReport.click()
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(5)
        elemBtnStep3 = driver.find_element_by_xpath("//div[@class='img step3']")
        elemBtnStep3.click()
        elemBtnAddPhoto = driver.find_element_by_xpath(".//*[@id='att_lists']/div[3]")
        elemBtnAddPhoto.send_keys("https://images-na.ssl-images-amazon.com/images/I/41pzTMUV7AL._SY300_.jpg")


    #def tearDown(self):
    #self.driver.close()

#if __name__ == "__main__":
    #unittest.main()