from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LandingPage(BasePage):
    search_box = (By.XPATH, "//textarea[@id='APjFqb']")
