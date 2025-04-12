import time

from pages.borrow_books_page import BorrowBooksPage


def test_borrow_books_link(driver):
    borrow_books_page = BorrowBooksPage()
    assert borrow_books_page.borrow_books_link.is_displayed(), "Borrowing Books link is not visible"
    assert borrow_books_page.borrow_books_link.is_enabled(), "Borrowing Books link is not enabled"
    borrow_books_page.borrow_books_link.click()


"""
Test Case: Verify that borrow books link is visible and clickable
    Step1: User is already on the home page
    Step2: Assert that the Borrowing Books link is visible
    Step3: Assert that the Borrowing Books link is enabled
    Step4: Click the Borrowing Books Link
    
Here is the xpath for locating the Borrowing Books Link element:
//a[@href='#borrowing-books']

"""
