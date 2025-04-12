import time

from pages.borrow_books_page import BorrowBooksPage


def test_borrow_books_link(driver):
    borrow_books_page = BorrowBooksPage()
    assert borrow_books_page.borrow_books_link.is_displayed()
    assert borrow_books_page.borrow_books_link.is_enabled()
    borrow_books_page.borrow_books_link.click()
    time.sleep(3)
