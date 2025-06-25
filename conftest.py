# conftest.py

import pytest
import yaml
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import setup_logger
from utils.environment import get_environment

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "config.yaml")

@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH, "r") as file:
        data = yaml.safe_load(file)
    return data

@pytest.fixture(scope="session", autouse=True)
def logger(config):
    log_level = config.get("logging", {}).get("level", "INFO").upper()
    log_file = config.get("logging", {}).get("file", "logs/test.log")
    logger = setup_logger(log_file_path=log_file, level=log_level)
    logger.info("===== Test Session Started =====")
    yield logger
    logger.info("===== Test Session Ended =====")

@pytest.fixture(scope="function")
def driver(config, logger):
    browser = config.get("browser", "chrome")
    headless = config.get("headless", False)

    if browser.lower() == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception(f"Browser {browser} is not supported")

    driver.implicitly_wait(config.get("implicit_wait", 10))
    yield driver
    driver.quit()



@pytest.fixture(scope="session", autouse=True)
def environment_info(logger):
    env = get_environment()
    logger.info(f"Test Environment: {env}")
