from src.main.core.Log import Log
from src.main.core.DriverWrapper import DriverWrapper

class PageNavigationUtil:
    @staticmethod
    def to(page_url: str):
        Log.log(f"Відкриваємо сторінку {page_url}")
        DriverWrapper.get_driver().navigate().to(page_url)
        Log.log(f"Відкрито сторінку {page_url}")
    @staticmethod
    def toMainPage():
        Log.log("Відкриваємо головну сторінку")
        DriverWrapper.get_driver().navigate().to("https://www.google.com")
        Log.log("Відкрито головну сторінку")
    @staticmethod
    def toSoftserve():
        Log.log("Відкриваємо сторінку SoftServe")
        DriverWrapper.get_driver().navigate().to("https://softserve.ua")
        Log.log("Відкрито сторінку SoftServe")
    @staticmethod
    def toEpam():
        Log.log("Відкриваємо сторінку Epam")
        DriverWrapper.get_driver().navigate().to("https://www.epam.com")
        Log.log("Відкрито сторінку Epam")
