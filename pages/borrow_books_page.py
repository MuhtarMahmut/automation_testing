from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BorrowBooksPage(BasePage):

    def __init__(self):
        super().__init__()
        self.borrow_books_link = self.find_element(By.XPATH, "//a[@href='#borrowing-books']")
