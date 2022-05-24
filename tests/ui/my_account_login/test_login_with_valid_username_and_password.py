import allure
from app.ui.steps.my_accout import MyAccount


@allure.suite("Suite: My Account - Login")
@allure.title("1. Login with valid username and password.")
@allure.testcase("http://practice.automationtesting.in/test-cases/#")
@allure.tag("Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_with_valid_username_and_password(home_page, browser_chrome):
    home_page.click_on_my_account_button()
    my_account = MyAccount(browser_chrome, browser_chrome.current_url)
    my_account.should_be_my_account_page()
