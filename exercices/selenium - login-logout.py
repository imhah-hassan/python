# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Formation\\Drivers\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.universitedutest.com/OrangeHRM"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("Paris$2018")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_xpath("//a[contains(@href, 'auth/logout')]").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()