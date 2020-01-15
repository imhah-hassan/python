from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# this Base class is serving basic attributes for every single page inherited from Page class
class Page(object):
    def __init__(self, driver, base_url='http://www.app.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        element = self.wait.until(EC.presence_of_element_located((locator)))
        return element

    def get_text(self, *locator):
        text = self.find_element(*locator).text
        return text

    def click (self, *locator):
        element = self.wait.until(EC.element_to_be_clickable((locator)))
        self.find_element(*locator).click()

    def type (self, *locator, value):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()