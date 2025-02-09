from src.main.core.DriverWrapper import DriverWrapper

class BasePage:
    def __init__(self):
        self.driver = DriverWrapper.get_driver()
