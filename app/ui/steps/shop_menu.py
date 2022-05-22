import allure
from app.ui.locators.locator_main_page import MainPageLocators
from configs.config import get_data
from framework.ui.base_page import BasePage


class ShopMenu(BasePage):

    get_url = get_data(file_name="browser_config.json")["shop_menu_url"]

    @allure.step("Check shop button")
    def check_shop_button(self):
        self.wait_element_located(*MainPageLocators.LOCATOR_SHOP_BUTTON).click()
