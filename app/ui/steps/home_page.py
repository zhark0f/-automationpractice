from random import choice

import allure
from app.ui.locators.locator_home_page import HomePageLocators
from configs.config import get_data
from framework.logger.logger import Logger
from framework.ui.base_page import BasePage
from framework.utils import asserts


class HomePage(BasePage):

    logger = Logger()
    home_page_url = get_data(file_name="browser_config.json")["home_page_url"]

    @allure.step("Open home page")
    def should_be_home_page(self):
        self.should_be_home_page_url()

    @allure.step("Check home page url is correct")
    def should_be_home_page_url(self):
        current_url = self.browser.current_url
        assert current_url in self.home_page_url, "whrong url for home page"

    @allure.step("Home page with three sliders only")
    def should_be_only_three_sliders(self):
        asserts.assert_equal(self.amount_sliders_on_the_home_page(), 3, "Amount sliders don't equal 3")

    @allure.step("Check is sliders on the home page")
    def amount_sliders_on_the_home_page(self):
        sliders_amount = len(self.wait_elements_located(*HomePageLocators.LOCATOR_SLIDERS))
        asserts.assert_not_equal(sliders_amount, 0, "Sliders aren't present on the home page")
        return sliders_amount

    @allure.step("Home page with three arrivals only")
    def should_be_only_three_arrivals(self):
        asserts.assert_equal(len(self.lisf_of_arrivals_on_the_home_page()), 3, "Amount arrivals don't equal 3")

    @allure.step("Check is arrivals on the home page")
    def lisf_of_arrivals_on_the_home_page(self):
        list_of_arrivals = self.wait_elements_located(*HomePageLocators.LOCATOR_ARRIVALS)
        asserts.assert_not_equal(len(list_of_arrivals), 0, "Arrivals don't present on the home page")
        return list_of_arrivals

    @allure.step("Ckick on the random arrivals")
    def click_on_the_random_arrivals(self):
        list_of_arrivals = self.lisf_of_arrivals_on_the_home_page()
        random_arrival = choice(list_of_arrivals)
        link_to_random_arrival = random_arrival.get_attribute('href')
        asserts.assert_true(link_to_random_arrival, "Link aren't present on the page")
        random_arrival.click()
        return link_to_random_arrival
