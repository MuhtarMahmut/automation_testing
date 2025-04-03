# utilities/element_actions.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.browser_manager import BrowserManager
from utilities.config_reader import ConfigReader


class ElementActions:
    driver = BrowserManager.get_driver()
    timeout = ConfigReader.getint("DEFAULT", "timeout")

    @classmethod
    def click(cls, locator):
        WebDriverWait(cls.driver, cls.timeout).until(EC.element_to_be_clickable(locator)).click()

    @classmethod
    def type(cls, locator, inputs):
        WebDriverWait(cls.driver, cls.timeout).until(EC.visibility_of_element_located(locator)).send_keys(inputs)

    @classmethod
    def clear(cls, locator):
        WebDriverWait(cls.driver, cls.timeout).until(EC.visibility_of_element_located(locator)).clear()

    @classmethod
    def get_text(cls, locator):
        return WebDriverWait(cls.driver, cls.timeout).until(EC.visibility_of_element_located(locator)).text

    @classmethod
    def is_displayed(cls, locator):
        return WebDriverWait(cls.driver, cls.timeout).until(EC.visibility_of_element_located(locator)).is_displayed()
