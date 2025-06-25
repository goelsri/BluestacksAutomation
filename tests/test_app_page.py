import requests
from pages.app_page import AppPage

def test_app_status_code():
    response = requests.get("https://www.bluestacks.com/apps/strategy/the-walking-dead-no-mans-land-on-pc.html")
    assert response.status_code == 200

# def test_app_page_title(driver):
#     app = AppPage(driver)
#     assert "BlueStacks" in app.get_title()

# def test_app_download_button_visible(driver):
#     app = AppPage(driver)
#     assert app.is_download_button_visible()
#
# def test_app_icon_present(driver):
#     app = AppPage(driver)
#     assert app.is_home_icon_visible()
