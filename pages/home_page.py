# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    DOWNLOAD_BTN = (By.CSS_SELECTOR, "a.btn-home-download")
    NAV_HOME_ICON = (By.CSS_SELECTOR, "a.logo")

    def __init__(self, driver):
        super().__init__(driver)

    def is_download_button_visible(self):
        return self.is_element_visible(*self.DOWNLOAD_BTN)

    def is_nav_home_icon_visible(self):
        return self.is_element_visible(*self.NAV_HOME_ICON)
