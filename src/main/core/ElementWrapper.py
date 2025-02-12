from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from DriverWrapper import *
from AutomationWait import *


class ElementWrapper:

    @staticmethod
    def find(by: By):
        """Знаходить елемент з використанням Fluent Wait"""
        wait = DriverWrapper.get_fluent_wait()
        return wait.until(lambda driver: AutomationWait.wait_visible_clickable(driver.find_element(by)))

    @staticmethod
    def find_one(by: By):
        """Знаходить один елемент без очікування"""
        return DriverWrapper.get_driver().find_element(by)

    @staticmethod
    def find_list(by: By) -> List:
        """Знаходить список елементів"""
        return DriverWrapper.get_driver().find_elements(by)
