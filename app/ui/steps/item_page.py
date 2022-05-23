import allure
from app.ui.locators.locator_item_page import ItemPageLocators
from framework.logger.logger import Logger
from framework.ui.base_page import BasePage
from framework.utils import asserts


class ItemPage(BasePage):

    logger = Logger()

    def __init__(self, link_to_the_item: str, browser, url: str):
        self.link_to_the_item = link_to_the_item
        super().__init__(browser, url)

    @allure.step("Open item page")
    def should_be_item_page(self):
        asserts.assert_true(self.should_be_item_page_url(), "something wrong with the item page")

    @allure.step("Check item page url is correct")
    def should_be_item_page_url(self):
        current_url = self.browser.current_url
        assert current_url in self.link_to_the_item, "whrong url for the item page"
        return True

    @allure.step("User can add item in basket")
    def user_can_add_arrivial_item_in_basket(self):
        self.basket_button_on_the_page()

    @allure.step("Check button 'ADD TO BASKET' on item page")
    def basket_button_on_the_page(self):
        asserts.assert_true(self.wait_element_located(*ItemPageLocators.LOCATOR_ADD_TO_BASKET).click(),
                            "Somethong wrong with button 'ADD TO BASKET'")
