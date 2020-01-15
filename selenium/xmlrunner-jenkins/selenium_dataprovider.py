# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
from unittest_data_provider import data_provider

class addEmployee(unittest.TestCase):
    employees = lambda: (
            (('0030','IMHAH', 'Hassan'),
            ('0031', 'DUMMERG', 'Patrick'), )
    )

    @classmethod
    def setUpClass(cls):
        print ('setUpClass')
        cls.driver = webdriver.Chrome('C:\\Users\\HIH\\Desktop\\Katalon\\02-WebDriver\\chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://localhost/orangehrm"
        cls.verificationErrors = []
        cls.accept_next_alert = True

    def test_a_login(self):
        print ('test_a_login')
        driver = self.driver
        driver.get(self.base_url)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'txtUsername')))
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("test")
        driver.find_element_by_id("btnLogin").click()
        self.assertEqual("Welcome Admin", driver.find_element_by_id("welcome").text)

    @data_provider(employees)
    def test_b_addEmployee(self, id, lastName, firstName):
        print ('test_b_addEmployee')
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_pim_viewPimModule')))
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_pim_addEmployee").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'firstName')))
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(lastName)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(firstName)
        if (id):
            driver.find_element_by_id("employeeId").clear()
            driver.find_element_by_id("employeeId").send_keys(id)
        driver.find_element_by_id("btnSave").click()
        try:
            try:
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='pdMainContainer']/div/h1")))
            except TimeoutException as ex:
                self.verificationErrors.append("Element not found by xpath //div[@id='pdMainContainer']/div/h1")
                return
            self.assertIsNotNone(element)
            if (element):
                self.assertEqual("Personal Details",
                         driver.find_element_by_xpath("//div[@id='pdMainContainer']/div/h1").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_y_deleteAllEmployee(self):
        print ('test_y_deleteAllEmployee')
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_pim_viewEmployeeList").click()
        driver.find_element_by_id("ohrmList_chkSelectAll").click()
        driver.find_element_by_id("btnDelete").click()
        driver.find_element_by_id("dialogDeleteBtn").click()

    def test_z_logout(self):
        print('test_z_logout')
        driver = self.driver
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_xpath("//a[contains(@href, 'auth/logout')]").click()

    @classmethod
    def tearDownClass(cls):
        print ('tearDownClass')
        cls.driver.quit()
        print (cls.verificationErrors)


if __name__ == "__main__":
    print("start\n")
    unittest.main()
    print("end\n")
