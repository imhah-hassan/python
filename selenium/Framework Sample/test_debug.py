# -*- coding: utf-8 -*-
from selenium import webdriver
from config import *
from utils import *
import pages
import unittest

class test_debug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(application["drivers"] + 'chromedriver.exe')
        cls.driver.get(application["url"])
        type (cls.driver, "txtUsername", application["username"])
        type (cls.driver, "txtPassword", application["password"])
        click (cls.driver, "btnLogin")

    def test_debug(self):
        driver = self.driver
        debug_page= pages.LeavePage(self)
        debug_page.add_leave_type("RTT")
        debug_page.add_leave_type(u"Congés sans solde")


    @classmethod
    def tearDownClass(cls):
        click (cls.driver, "welcome")
        click (cls.driver, "//div[@id='welcome-menu']/ul/li[3]/a")
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
