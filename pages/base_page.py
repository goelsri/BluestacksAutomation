# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            logging.error(f"Element {locator} not clickable")

    def type(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            logging.error(f"Element {locator} not visible to type")

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            logging.error(f"Element {locator} not visible to get text")
            return ""

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
