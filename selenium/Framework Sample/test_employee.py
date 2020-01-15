# -*- coding: utf-8 -*-
from selenium import webdriver
from config import *
import pages
import unittest

class test_employee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(application["drivers"] + 'chromedriver.exe')
        cls.driver.get(application["url"])

    def test_a_login(self):
        login_page = pages.LoginPage (self)
        login_page.connect()

    # @unittest.skip  # no reason needed
    def test_b_delete_all_employee(self):
        employee_list_page = pages.EmployeeListPage(self)
        employee_list_page.delete_all_employee()

    # @unittest.skip  # no reason needed
    def test_c_add_employee(self):
        employee_page = pages.EmployeePage(self)
        employee_page.add_employee()

    def test_d_view_employee(self):
        employee_list_page = pages.EmployeeListPage(self)
        employee_list_page.view_employee("0991")

    def test_e_employee_address(self):
        employee_page = pages.EmployeePage(self)
        employee_page.employee_address()

    def test_z_logout(self):
        home_page = pages.HomePage (self)
        home_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
