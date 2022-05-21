from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:

    def __init__(self, browser: webdriver.Chrome, url: str):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)

    def wait_element_clickable(self, find_by, locator, timeout=15):
        button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((find_by, locator))
        )
        return button

    def wait_element_located(self, find_by, locator, timeout=15):
        button = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((find_by, locator))
        )
        return button

    def wait_elements_located(self, find_by, locator, timeout=15):
        buttons = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located((find_by, locator))
        )
        return buttons

    def wait_for_url(self, url, timeout=15):
        button = WebDriverWait(self.browser, timeout).until(
            EC.url_to_be(url)
        )
        return button

    def text_to_be_present_in_element(
            self, find_by: object, locator: object, text: str, timeout: object = 15) -> object:
        element = WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element((find_by, locator), text)
        )
        return element
