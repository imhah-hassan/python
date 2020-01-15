from PageObject.base import Page
from PageObject.locators import *


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginLocators
        super().__init__(driver)

    def login(self, username, password):
        self.type(*self.locator.USERNAME, value=username)
        self.type(*self.locator.PASSWORD, value=password)
        self.click(*self.locator.BTN_LOGIN)

    def get_message(self):
        return self.get_text(*self.locator.LB_MESSAGE)


class HomePage(Page):
    def __init__(self, driver):
        self.locator = HomeLocators
        super().__init__(driver)

    def get_welcome_message(self):
        return self.get_text(*self.locator.MN_WELCOME)

    def logout(self):
        self.click(*self.locator.MN_WELCOME)
        self.click(*self.locator.MN_LOGOUT)

class AddEmployeePage(Page):
    def __init__(self, driver):
        self.locator = AddEmployeeLocators
        super().__init__(driver)

    def add_employee(self, firstName, lastName, employeeID):
        self.click(*self.locator.MN_PIM)
        self.click(*self.locator.MN_ADD_EMPLOYEE)
        self.type(*self.locator.FIRST_NAME, value=firstName)
        self.type(*self.locator.LAST_NAME, value=lastName)
        self.type(*self.locator.EMPLOYEE_ID, value=employeeID)
        self.click(*self.locator.BTN_EDIT_SAVE)

    def get_title(self):
        return self.get_text(*self.locator.LB_TITLE)



