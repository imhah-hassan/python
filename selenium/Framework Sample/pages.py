from config import *
from utils import *

class BasePage(object):
    def __init__(self, testcase):
        self.testcase = testcase
        self.driver = testcase.driver

class LoginPage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def connect(self):
        driver = self.driver
        type (driver, "txtUsername", application["username"])
        type (driver, "txtPassword", application["password"])
        click (driver, "btnLogin")
        check_text(self.testcase, driver, "welcome", "Welcome Admin" )

class HomePage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def logout(self):
        driver = self.driver
        click (driver, "welcome")
        click (driver, "//div[@id='welcome-menu']/ul/li[3]/a")
        check_present (self.testcase, driver, "txtUsername")

class EmployeePage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def add_employee(self):
        driver = self.driver
        click (driver, "menu_pim_viewPimModule")
        click (driver, "menu_pim_addEmployee")
        type (driver, "firstName", "IMHAH")
        type (driver, "middleName", "hih")
        type (driver, "lastName", "Hassan")
        type (driver, "employeeId", "0991")
        # add login
        click (driver, "chkLogin")
        type (driver, "user_name", "himhah")
        type (driver, "user_password", "acial")
        type (driver, "re_password", "acial")
        # save
        click (driver, "btnSave")
        # check
        check_text(self.testcase, driver, "//div[@id='pdMainContainer']/div/h1", "Détails personnels" )
        check_text(self.testcase, driver, "//div[@id='profile-pic']/h1", "IMHAH Hassan" )


    def employee_address(self):
        driver = self.driver
        click (driver, u"Coordonnées")
        click (driver, "btnSave")
        type (driver, "contact_street1", u"20 rue d'athènes")
        type (driver, "contact_city", "Paris")
        type (driver, "contact_province", "Paris")
        type (driver, "contact_emp_zipcode", "75009")
        select_text(driver, "contact_country", "France")
        type (driver, "contact_emp_hm_telephone", "0155335240")
        type (driver, "contact_emp_mobile", "0155335210")
        type (driver, "contact_emp_work_telephone", "0155665577")
        type (driver, "contact_emp_work_email", "0211@work.org")
        type (driver, "contact_emp_oth_email", "sdfsdf@work.org")
        click (driver, "btnSave")
        check_value(self.testcase, driver, "contact_city", "Paris" )

class EmployeeListPage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def delete_all_employee(self):
        driver = self.driver
        click (driver, "menu_pim_viewPimModule")
        click (driver, "menu_pim_viewEmployeeList")
        nbLignes = len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        if (nbLignes>0):
            click (driver, "ohrmList_chkSelectAll")
            click (driver, "btnDelete")
            click (driver, "dialogDeleteBtn")
            check_text(self.testcase, driver, "//table[@id='resultTable']/tbody/tr/td", u"Aucun résultat" )

    def search_employee(self, id):
        driver = self.driver
        click (driver, "menu_pim_viewPimModule")
        click (driver, "menu_pim_viewEmployeeList")
        type (driver, "empsearch_id", id)
        click(driver, "searchBtn")
        return (len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")))

    def view_employee(self, id):
        driver = self.driver
        count = self.search_employee(id)
        self.testcase.assertGreater (count, 0)
        if (self.search_employee(id)>=0):
            click (driver, id)
            check_text(self.testcase, driver, "//div[@id='pdMainContainer']/div/h1", "Détails personnels" )
            check_text(self.testcase, driver, "//div[@id='profile-pic']/h1", "IMHAH hih Hassan" )

class LocalizationPage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def change_language(self):
        driver = self.driver
        click (driver, "menu_admin_viewAdminModule")
        click (driver, "menu_admin_Configuration")
        click (driver, "menu_admin_localization")
        click (driver, "btnSave")
        select_text(driver, "localization_dafault_language", "French - France")
        click (driver, "btnSave")
        check_value(self.testcase, driver, "localization_dafault_language", "fr_FR")

class LeavePage(BasePage):
    def __init__(self, testcase):
        BasePage.__init__(self, testcase)

    def define_leave_period(self):
        driver = self.driver
        driver.find_element_by_id("menu_leave_viewLeaveModule").click()
        driver.find_element_by_id("menu_leave_Configure").click()
        driver.find_element_by_id("menu_leave_defineLeavePeriod").click()
        driver.find_element_by_id("btnEdit").click()
        Select(driver.find_element_by_id("leaveperiod_cmbStartMonth")).select_by_visible_text("Juin")
        Select(driver.find_element_by_id("leaveperiod_cmbStartDate")).select_by_visible_text("1")
        driver.find_element_by_id("btnEdit").click()
        self.testcase.assertEqual("May 31", driver.find_element_by_id("lblEndDate").text)

    def delete_all_leave_type(self):
        driver = self.driver
        driver.find_element_by_id("menu_leave_viewLeaveModule").click()
        driver.find_element_by_id("menu_leave_Configure").click()
        driver.find_element_by_id("menu_leave_leaveTypeList").click()
        rows_count= len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        if rows_count>1:
            driver.find_element_by_id("ohrmList_chkSelectAll").click()
            driver.find_element_by_id("btnDelete").click()
            driver.find_element_by_id("dialogDeleteBtn").click()
        rows_count= len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        self.testcase.assertEqual(1, rows_count)

    def add_leave_type(self, leave_type):
        driver = self.driver
        found = False
        driver.find_element_by_id("menu_leave_viewLeaveModule").click()
        driver.find_element_by_id("menu_leave_Configure").click()
        driver.find_element_by_id("menu_leave_leaveTypeList").click()
        rows_count= len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        if (driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr/td").text != "Aucun résultat"):
            for i in range(1, rows_count+1):
                __leave_type = driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr["+str(i)+"]/td[2]/a").text
                if (leave_type == __leave_type ):
                    found = True
                    break
        else:
            rows_count=0
        if ( not found ):
            driver.find_element_by_id("btnAdd").click()
            driver.find_element_by_id("leaveType_txtLeaveTypeName").clear()
            driver.find_element_by_id("leaveType_txtLeaveTypeName").send_keys(leave_type)
            driver.find_element_by_id("leaveType_excludeIfNoEntitlement").click()
            driver.find_element_by_id("saveButton").click()
            # OrangeHRM - Confirmation requise
            if is_element_present(driver, "//div[@id='undeleteDialog']/div/h3"):
                driver.find_element_by_id("undeleteYes").click()
            new_rows_count = len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
            self.testcase.assertEqual(new_rows_count , rows_count + 1)
        else:
            new_rows_count = len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
            self.testcase.assertEqual(new_rows_count , rows_count)

