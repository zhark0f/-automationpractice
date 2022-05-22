from app.ui.steps.shop_menu import ShopMenu


class TestSuiteHomePage:

    @staticmethod
    def test_home_page_with_three_sliders_only(open_browser_chrome):
        shop_page = ShopMenu(open_browser_chrome, ShopMenu.get_url)
        shop_page.open()
        shop_page.check_shop_button()
