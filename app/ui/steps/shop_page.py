import allure
from configs.config import get_data
from framework.logger.logger import Logger
from framework.ui.base_page import BasePage


class ShopPage(BasePage):

    logger = Logger()
    shop_page_url = get_data(file_name="browser_config.json")["shop_menu_url"]

    @allure.step("Open main page")
    def should_be_shop_page(self):
        self.should_be_shop_page_url()

    @allure.step("Check shop page url is correct")
    def should_be_shop_page_url(self):
        current_url = self.browser.current_url
        assert current_url in self.shop_page_url, "whrong url for shop page"
