from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities.config_reader import ConfigReader


class BrowserManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            browser = ConfigReader.get('DEFAULT', 'browser').lower()

            if browser == "chrome":
                options = Options()
                options.add_argument("--start-maximized")
                cls._driver = webdriver.Chrome(options=options)

            elif browser == "firefox":
                options = FirefoxOptions()
                cls._driver = webdriver.Firefox(options=options)

            else:
                raise Exception(f"Browser '{browser}' is not supported.")

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
