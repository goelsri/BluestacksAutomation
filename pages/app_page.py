from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AppPage(BasePage):
    DOWNLOAD_BTN = (By.CSS_SELECTOR, "a[data-v-7aa3bb54][href*='downloads']")
    HOME_ICON = (By.CSS_SELECTOR, "a.logo")

    def __init__(self, driver, config):
        super().__init__(driver)
        self.driver.get(config["base_url"]["app page"])

    def is_download_button_visible(self):
        return self.is_element_visible(*self.DOWNLOAD_BTN)

    def is_home_icon_visible(self):
        return self.is_element_visible(*self.HOME_ICON)
