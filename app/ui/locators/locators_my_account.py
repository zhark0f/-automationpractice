from selenium.webdriver.common.by import By


class MyAccountLocators:

    LOCATOR_LOGIN_FORM = (By.CSS_SELECTOR, "form.login")
    LOCATOR_REGISTER_FORM = (By.CSS_SELECTOR, "form.register")
