# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        print ('setUp')
        self.driver = webdriver.Chrome('C:\\Users\\HIH\\Desktop\\Katalon\\02-WebDriver\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/orangehrm"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_a_login_logout(self):
        print ('test_a_login_logout')
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("test")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_xpath("//a[contains(@href, 'auth/logout')]").click()

    def tearDown(self):
        print ('tearDown')
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()