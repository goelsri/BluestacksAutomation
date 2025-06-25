# tests/test_app.py

import requests
import pytest
from pages.app_page import AppPage

@pytest.mark.smoke
@pytest.mark.functional
def test_app_status_code(config):
    response = requests.get(config["base_urls"]["app"])
    assert response.status_code == 200

@pytest.mark.regression
def test_app_title(driver, config):
    driver.get(config["base_urls"]["app"])
    assert "The Walking Dead: No Man’s Land" in driver.title

# @pytest.mark.smoke
def test_app_download_button(driver, config):
    driver.get(config["base_urls"]["app"])
    page = AppPage(driver)
    assert page.is_download_button_visible()

@pytest.mark.functional
def test_app_nav_icon(driver, config):
    driver.get(config["base_urls"]["app"])
    page = AppPage(driver)
    assert page.is_nav_home_icon_visible()
