from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_element_visible(self, by, locator):
        try:
            return self.driver.find_element(by, locator).is_displayed()
        except:
            return False

    def get_title(self):
        return self.driver.title
