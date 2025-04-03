import pytest
import os
from datetime import datetime
from utilities.browser_manager import BrowserManager
from utilities.config_reader import ConfigReader


@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Starting the browser...")
    driver = BrowserManager.get_driver()
    timeout = ConfigReader.getint('DEFAULT', 'timeout')
    driver.implicitly_wait(timeout)
    driver.get(ConfigReader.get("DEFAULT", "base_url"))
    yield driver
    print("\n[Teardown] Quitting the browser...")
    BrowserManager.quit_driver()



def pytest_runtest_setup(item):
    print(f"\n[TEST] Running: {item.name}")


def pytest_configure(config):
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join("screenshots", file_name)
            driver.save_screenshot(file_path)
            print(f"\n[!] Screenshot saved to: {file_path}")
