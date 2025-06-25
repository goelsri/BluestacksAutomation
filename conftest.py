import pytest
import yaml
from selenium import webdriver
from utils.logger import setup_logger

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session", autouse=True)
def start_logging():
    setup_logger()

@pytest.fixture()
def driver(config):
    options = webdriver.ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config["implicit_wait"])
    yield driver
    driver.quit()
