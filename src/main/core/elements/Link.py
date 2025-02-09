from selenium.webdriver.remote.webelement import WebElement


class Link(WebElement):
    def __init__(self, base: WebElement, parent, id_):
        super().__init__(parent, id_)
        self.base = base

    def click(self):
        self.base.click()

    def get_text(self):
        return self.base.text
