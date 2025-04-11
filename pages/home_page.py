from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.user_profile_link = self.find_element(By.XPATH, "//a[@id='navbarDropdown']")
        self.books_link = self.find_element(By.XPATH, "//a[@href='#books']")