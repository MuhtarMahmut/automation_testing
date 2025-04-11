from abc import ABC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from utilities.browser_manager import BrowserManager


class BasePage(ABC):
    def __init__(self):
        self.driver = BrowserManager.get_driver()

    def find_element(self, by: By, value: str) -> WebElement:
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        return self.driver.find_elements(by, value)
