# tests/test_home.py

import requests
import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.functional
def test_home_status_code(config):
    response = requests.get(config["base_urls"]["home"])
    assert response.status_code == 200

@pytest.mark.regression
def test_home_title(driver, config):
    driver.get(config["base_urls"]["home"])
    assert "BlueStacks – Best Mobile Gaming Platform for PC & Mac" in driver.title

# @pytest.mark.smoke
def test_home_download_button(driver, config):
    driver.get(config["base_urls"]["home"])
    page = HomePage(driver)
    assert page.is_download_button_visible()

@pytest.mark.functional
def test_home_nav_icon(driver, config):
    driver.get(config["base_urls"]["home"])
    page = HomePage(driver)
    assert page.is_nav_home_icon_visible()
