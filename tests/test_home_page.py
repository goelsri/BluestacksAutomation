import requests
from pages.home_page import HomePage

def test_home_status_code(config):
    response = requests.get(config["base_urls"]["home"])
    assert response.status_code == 200

# def test_home_title(driver, config):
#     page = HomePage(driver, config["base_urls"]["home"])
#     assert "BlueStacks" in page.get_title()
#
# def test_home_download_button(driver, config):
#     page = HomePage(driver, config["base_urls"]["home"])
#     assert page.is_download_button_visible()
#
# def test_home_icon(driver, config):
#     page = HomePage(driver, config["base_urls"]["home"])
#     assert page.is_home_icon_visible()
