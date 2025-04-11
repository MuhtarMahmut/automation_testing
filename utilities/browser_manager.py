from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities.config_reader import ConfigReader


class BrowserManager:
    _driver = None

    @classmethod
    def get_driver(cls):

        if not cls._driver:
            browser = ConfigReader.get_config('Default', 'browser').lower()
            headless = ConfigReader.get_config('Default', 'headless').lower()

            if browser == "chrome":
                options = Options()
                options.add_argument("--start-maximized")
                if headless == 'true':
                    options.add_argument("--headless")
                    options.add_argument("--disable-gpu")
                cls._driver = webdriver.Chrome(options=options)

            elif browser == "firefox":
                options = FirefoxOptions()
                if headless == 'true':
                    options.add_argument("--headless")
                cls._driver = webdriver.Firefox(options=options)

            else:
                raise Exception(f"Browser '{browser}' is not supported.")

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
