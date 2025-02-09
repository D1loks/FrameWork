from selenium.webdriver.remote.webelement import WebElement

class Button:
    def __init__(self, base: WebElement):
        self.base = base

    def click(self):
        self.base.click()

    def get_button_text(self) -> str:
        """Повертає значення атрибута aria-label (якщо він є)"""
        return self.base.get_attribute("aria-label")

    def get_base(self) -> WebElement:
        """Повертає сам WebElement"""
        return self.base

    def get_text(self) -> str:
        """Повертає текст кнопки"""
        return self.base.text
