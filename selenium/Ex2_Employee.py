# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Apps\\SeleniumDrivers\\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://localhost/orangehrm"
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_a_login(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")

        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("T€st$2020")

        element = self.wait.until(EC.element_to_be_clickable((By.ID, 'frmLogin')))
        element = self.wait.until(EC.presence_of_element_located( (By.ID, 'frmLogin') ))
        driver.find_element_by_id("frmLogin").submit()

        self.assertEqual("Bienvenue Hassan", driver.find_element_by_id("welcome").text)

    def test_b_add_employe(self):
        driver = self.driver
        pimMenu = self.wait.until(EC.element_to_be_clickable((By.ID, 'menu_pim_viewPimModule')))
        pimMenu.click()
        addEmployeeMenu = self.wait.until(EC.element_to_be_clickable((By.ID, 'menu_pim_addEmployee')))
        addEmployeeMenu.click()

        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Hassan")

        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("IMHAH")

        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys("0102")

        driver.find_element_by_id("btnSave").click()
        self.assertEqual("Hassan IMHAH",
        driver.find_element_by_xpath("//div[@id='profile-pic']/h1").text)

        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_id("personal_optGender_1").click()
        Select(driver.find_element_by_id("personal_cmbNation")).select_by_visible_text("Français")
        Select(driver.find_element_by_id("personal_cmbMarital")).select_by_visible_text("Marié")
        driver.find_element_by_id("personal_DOB").clear()
        driver.find_element_by_id("personal_DOB").send_keys("1978-02-13")
        driver.find_element_by_id("btnSave").click()
        self.assertEqual("Hassan",
                             driver.find_element_by_id("personal_txtEmpFirstName").get_attribute("value"))

    def test_c_delete_employees(self):
        driver = self.driver
        pimMenu = self.wait.until(EC.element_to_be_clickable((By.ID, 'menu_pim_viewPimModule')))
        pimMenu.click()
        listEmployeeMenu = self.wait.until(EC.element_to_be_clickable((By.ID, 'menu_pim_viewEmployeeList')))
        listEmployeeMenu.click()
        driver.find_element_by_id("empsearch_id").clear()
        driver.find_element_by_id("empsearch_id").send_keys("0102")
        driver.find_element_by_id("searchBtn").click()
        rows = len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        if (rows == 1):
            result = driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr/td").text

        if (result != "Aucun résultat"):
            driver.find_element_by_id("ohrmList_chkSelectAll").click()
            driver.find_element_by_id("btnDelete").click()
            driver.find_element_by_id("dialogDeleteBtn").click()

        self.assertEqual("Aucun Résultat",
                        driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr/td").text)

    def test_z_logout(self):
        driver = self.driver
        welcomeMenu = self.wait.until(EC.element_to_be_clickable((By.ID, 'welcome')))
        welcomeMenu.click()
        logoutMenu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/index.php/auth/logout')]")))
        logoutMenu.click()

        self.assertEqual("LOGIN Groupe", driver.find_element_by_id("logInPanelHeading").text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present (self, xpath):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return (True)
        except AssertionError as e:
            return (False)

    def is_clickable (self, xpath):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return (True)
        except AssertionError as e:
            return (False)

if __name__ == "__main__":
    unittest.main()
