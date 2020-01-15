from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def wait_for_element_present(driver, element):
    for i in range(1,2) :
        try:
            WebDriverWait(driver, 0.05).until( EC.visibility_of_element_located( (By.ID, element) ) )
            return (driver.find_element_by_id(element))
        except TimeoutException as e:
            try:
                WebDriverWait(driver, 0.05).until( EC.visibility_of_element_located( (By.XPATH, element) ) )
                return (driver.find_element_by_xpath(element))
            except TimeoutException as e:
                try:
                    WebDriverWait(driver, 0.05).until( EC.visibility_of_element_located( (By.CSS_SELECTOR, element) ) )
                    return (driver.find_element_by_css(element))
                except TimeoutException as e:
                    try:
                        WebDriverWait(driver, 0.05).until( EC.visibility_of_element_located( (By.LINK_TEXT, element) ) )
                        return (driver.find_element_by_link_text(element))
                    except TimeoutException as e:
                        try:
                            WebDriverWait(driver, 0.05).until( EC.visibility_of_element_located( (By.PARTIAL_LINK_TEXT, element) ) )
                            return (driver.find_element_by_partial_link_text(element))
                        except TimeoutException as e:
                            continue
    raise NoSuchElementException


def click (driver, element):
    el = wait_for_element_present(driver, element)
    el.click()

def type (driver, element, text):
    el = wait_for_element_present(driver, element)
    el.clear()
    el.send_keys(text)

def select_text (driver, element, text):
    el = wait_for_element_present(driver, element)
    Select(el).select_by_visible_text(text)

def check_text (testcase, driver, element, text):
    el = wait_for_element_present(driver, element)
    testcase.assertEqual(el.text, text)

def check_value (testcase, driver, element, value):
    el = wait_for_element_present(driver, element)
    testcase.assertEqual(el.get_attribute("value"), value)

def check_present (testcase, driver, element):
    testcase.assertTrue (is_element_present(driver, element))

def is_element_present(driver, element):
    try:
        el=wait_for_element_present(driver, element)
    except NoSuchElementException as e:
        return False
    return True
