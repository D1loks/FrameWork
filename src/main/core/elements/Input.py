from selenium.webdriver.remote.webelement import WebElement
from typing import Optional

class Input:
    def __init__(self, base: WebElement):
        self.base = base

    def write(self, text: str) -> None:
        self.base.send_keys(text)

    def get_search_title(self) -> Optional[str]:
        return self.base.get_attribute("title")

    def submit(self) -> None:
        self.base.submit()
