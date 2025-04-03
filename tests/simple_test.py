# tests/test_google_search.py

import pytest
from pages.landing_page import LandingPage
from utilities.element_actions import ElementActions
from utilities.wait_utils import WaitUtils
from selenium.webdriver.common.keys import Keys

def test_google_search(driver):
    landing_page = LandingPage(driver)
    # Wait for the search box to be visible
    WaitUtils.wait_for_element_visible(landing_page.search_box)

    # Type "Selenium Automation" and press Enter
    ElementActions.type(landing_page.search_box, "Selenium Automation" + Keys.ENTER)

    # Optional: assert that results page loaded
#    WaitUtils.wait_for_title("Selenium Automation")
#    assert "Selenium Automation" in driver.title
