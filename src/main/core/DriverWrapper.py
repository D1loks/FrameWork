import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import FluentWait

class DriverWrapper:
    _driver = None
    _wait = None

    def __init__(self):
        driver_type = self.get_property("driver")
        if driver_type == "Chrome":
            chrome_service = ChromeService(ChromeDriverManager().install())
            base_driver = webdriver.Chrome(service=chrome_service)
        elif driver_type == "Firefox":
            firefox_service = FirefoxService(GeckoDriverManager().install())
            base_driver = webdriver.Firefox(service=firefox_service)
        else:
            raise ValueError(f"Unsupported driver type: {driver_type}")

        self._driver = EventFiringWebDriver(base_driver, MyEventListener())

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls()
        return cls._driver

    @classmethod
    def get_fluent_wait(cls):
        if cls._wait is None:
            cls._wait = WebDriverWait(cls.get_driver(), 30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
        return cls._wait

    @staticmethod
    def get_property(property_name):
        properties = {
            "driver": "Chrome"  # Замініть на реальне читання з файлу або змінної оточення
        }
        return properties.get(property_name, None)
