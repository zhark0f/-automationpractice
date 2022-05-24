import allure
from app.ui.locators.locators_my_account import MyAccountLocators
from configs.config import get_data
from framework.logger.logger import Logger
from framework.ui.base_page import BasePage
from framework.utils import asserts
from selenium.common.exceptions import NoSuchElementException


class MyAccount(BasePage):

    logger = Logger()
    my_account_page_url = get_data(file_name="browser_config.json")["my_account_page_url"]

    @allure.step("Open my account page")
    def should_be_my_account_page(self):
        self.should_be_my_account_page_url()
        asserts.assert_true(self.should_be_login_form_and_register_form(), "Something whrong with my account page")

    @allure.step("Check my account page url is correct")
    def should_be_my_account_page_url(self):
        current_url = self.browser.current_url
        assert current_url in self.my_account_page_url, "whrong url for my account page"

    @allure.step("Check if the login form is present")
    def should_be_login_form_and_register_form(self):
        try:
            self.browser.find_element(*MyAccountLocators.LOCATOR_LOGIN_FORM)
            self.browser.find_element(*MyAccountLocators.LOCATOR_REGISTER_FORM)
        except NoSuchElementException:
            return False
        return True
