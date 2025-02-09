from selenium.webdriver.remote.webelement import WebElement

class Label:
    def __init__(self, base: WebElement):
        self.base = base

    def get_label_text(self) -> str:
        return self.base.text
