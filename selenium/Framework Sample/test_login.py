# -*- coding: utf-8 -*-
from selenium import webdriver
from config import *
import pages
import unittest

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(application["drivers"] + 'chromedriver.exe')
        cls.driver.get(application["url"])

    def test_a_login(self):
        login_page = pages.LoginPage (self)
        login_page.connect()

    def test_z_logout(self):
        home_page = pages.HomePage (self)
        home_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
