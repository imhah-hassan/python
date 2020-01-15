# -*- coding: utf-8 -*-
from selenium import webdriver
from config import *
from utils import *
import pages
import unittest
from unittest_data_provider import data_provider
class test_configuration(unittest.TestCase):
    leave_types = lambda: (
                            ('RTT',),
                            (u'Congés payés',),
                            (u'Congé maternité',),
                            (u'Congé sans solde',),
                    )

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(application["drivers"] + 'chromedriver.exe')
        cls.driver.get(application["url"])

    def test_a_login(self):
        login_page = pages.LoginPage (self)
        login_page.connect()

    # @unittest.skip  # no reason needed
    def test_b_localization(self):
        driver = self.driver
        localization_page= pages.LocalizationPage(self)
        localization_page.change_language()

    # @unittest.skip  # no reason needed
    def test_c_define_leave_period(self):
        driver = self.driver
        leave_page= pages.LeavePage(self)
        leave_page.define_leave_period()

    def test_d_delete_all_leave_type(self):
        driver = self.driver
        leave_page= pages.LeavePage(self)
        leave_page.delete_all_leave_type()

    # @unittest.skip  # no reason needed
    @data_provider(leave_types)
    def test_e_add_leave_type(self, leave_type):
        driver = self.driver
        leave_page= pages.LeavePage(self)
        leave_page.add_leave_type(leave_type)

    def test_z_logout(self):
        home_page = pages.HomePage (self)
        home_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
