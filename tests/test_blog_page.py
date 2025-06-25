import requests
from pages.blog_page import BlogPage

def test_blog_status_code():
    response = requests.get("https://www.bluestacks.com/blog/games/three-kingdoms-overlord.html")
    assert response.status_code == 200

# def test_blog_page_title(driver):
#     blog = BlogPage(driver)
#     assert "BlueStacks" in blog.get_title()

# def test_blog_download_button_visible(driver):
#     blog = BlogPage(driver)
#     assert blog.is_download_button_visible()
#
# def test_blog_icon_present(driver):
#     blog = BlogPage(driver)
#     assert blog.is_home_icon_visible()
