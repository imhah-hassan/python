from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginLocators(object):
  USERNAME      = (By.ID, 'txtUsername')
  PASSWORD      = (By.ID, 'txtPassword')
  BTN_LOGIN     = (By.ID, 'btnLogin')
  LB_MESSAGE    = (By.ID, 'spanMessage')

class HomeLocators(object):
  MN_WELCOME        = (By.ID, 'welcome')
  MN_LOGOUT         = (By.XPATH, '//a[contains(@href, \'auth/logout\')]')

class AddEmployeeLocators(object):
  MN_PIM = (By.ID, 'menu_pim_viewPimModule')
  MN_ADD_EMPLOYEE = (By.ID, 'menu_pim_addEmployee')
  FIRST_NAME        = (By.ID, 'firstName')
  LAST_NAME         = (By.ID, 'lastName')
  EMPLOYEE_ID       = (By.ID, 'employeeId')
  BTN_EDIT_SAVE     = (By.ID, 'btnSave')
  LB_TITLE = (By.XPATH, '//div[@id=\'profile-pic\']/h1')

class EmployeeDetailLocators(object):
  BTN_EDIT_SAVE     = (By.ID, 'btnSave')
  RB_GENDRE_MALE    = (By.ID, 'personal_optGender_1')
  RB_GENDRE_FEMALE  = (By.ID, 'personal_optGender_2')
  RB_GENDRE_FEMALE  = (By.ID, 'personal_optGender_2')
  LST_NATION        = (By.ID, 'personal_cmbNation')
  LST_MARITAL_STATUS= (By.ID, 'personal_cmbMarital')
  FIST_NAME         = (By.ID, 'personal_txtEmpFirstName')
