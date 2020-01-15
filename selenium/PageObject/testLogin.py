# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from PageObject.pages import *

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("C:\\Apps\\SeleniumDrivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/orangehrm"
        self.driver.get(self.base_url)

    def test_a_login_ko(self):
        page = LoginPage(self.driver)
        page.login('admin', '123456789')
        self.assertEqual(page.get_message(), "Identifiants Non Valides")

    def test_b_login(self):
        page = LoginPage(self.driver)
        page.login('admin', 'T€st$2020')
        page = HomePage(self.driver)
        self.assertEqual(page.get_welcome_message(), "Bienvenue Hassan")

    def test_c_add_employee(self):
        page = AddEmployeePage(self.driver)
        page.add_employee('IMHAH', 'Hassan', '1001')
        self.assertEqual(page.get_title(), "IMHAH Hassan")

    def test_z_logout(self):
        home = HomePage(self.driver)
        home.logout()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()