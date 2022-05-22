from app.ui.steps.home_page import HomePage
from app.ui.steps.shop_page import ShopPage


class TestSuiteHomePage:

    @staticmethod
    def test_home_page_should_be_with_three_sliders_only(browser_chrome):
        home_page = HomePage(browser_chrome, HomePage.home_page_url)
        home_page.open()
        home_page.should_be_home_page()
        home_page.click_on_shop_button()
        shop_page = ShopPage(browser_chrome, browser_chrome.current_url)
        shop_page.should_be_shop_page()
        shop_page.click_on_home_page_button()
        home_page = HomePage(browser_chrome, browser_chrome.current_url)
        home_page.should_be_home_page()
        home_page.should_be_only_three_sliders()
