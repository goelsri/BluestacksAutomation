# tests/test_blog.py

import requests
import pytest
from pages.blog_page import BlogPage

@pytest.mark.smoke
@pytest.mark.functional
def test_blog_status_code(config):
    response = requests.get(config["base_urls"]["blog"])
    assert response.status_code == 200

@pytest.mark.regression
def test_blog_title(driver, config):
    driver.get(config["base_urls"]["blog"])
    assert "Three Kingdoms Overlord" in driver.title

# @pytest.mark.smoke
def test_blog_download_button(driver, config):
    driver.get(config["base_urls"]["blog"])
    page = BlogPage(driver)
    assert page.is_download_button_visible()

@pytest.mark.functional
def test_blog_nav_icon(driver, config):
    driver.get(config["base_urls"]["blog"])
    page = BlogPage(driver)
    assert page.is_nav_home_icon_visible()
