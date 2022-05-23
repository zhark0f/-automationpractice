import allure
import pytest
from app.ui.steps.home_page import HomePage
from app.ui.steps.item_page import ItemPage
from app.ui.steps.shop_page import ShopPage


@pytest.mark.xfail(reason="User can't add item in basket, but he should. Bug number in Jira: .....")
@allure.suite("Suite: Home Page")
@allure.title("3. Home page - Images in Arrivals should navigate")
@allure.testcase("http://practice.automationtesting.in/test-cases/#")
@allure.tag("Home page")
def test_home_page_should_be_with_three_arrivals_only(home_page, browser_chrome):
    home_page.click_on_shop_button()
    shop_page = ShopPage(browser_chrome, browser_chrome.current_url)
    shop_page.should_be_shop_page()
    shop_page.click_on_home_page_button()
    home_page = HomePage(browser_chrome, browser_chrome.current_url)
    home_page.should_be_home_page()
    home_page.should_be_only_three_arrivals()
    link_to_item = home_page.click_on_the_random_arrivals()
    item_page = ItemPage(link_to_item, browser_chrome, browser_chrome.current_url)
    item_page.should_be_item_page()
    item_page.user_can_add_arrivial_item_in_basket()
