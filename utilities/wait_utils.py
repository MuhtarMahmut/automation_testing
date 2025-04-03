# utilities/wait_utils.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.browser_manager import BrowserManager
from utilities.config_reader import ConfigReader


class WaitUtils:
    driver = BrowserManager.get_driver()
    timeout = ConfigReader.getint('DEFAULT', 'timeout')

    @classmethod
    def wait_for_title(cls, title_text):
        WebDriverWait(cls.driver, cls.timeout).until(EC.title_contains(title_text))

    @classmethod
    def wait_for_url(cls, partial_url):
        WebDriverWait(cls.driver, cls.timeout).until(EC.url_contains(partial_url))

    @classmethod
    def wait_for_element_visible(cls, locator):
        return WebDriverWait(cls.driver, cls.timeout).until(EC.visibility_of_element_located(locator))

    @classmethod
    def wait_for_element_clickable(cls, locator):
        return WebDriverWait(cls.driver, cls.timeout).until(EC.element_to_be_clickable(locator))
