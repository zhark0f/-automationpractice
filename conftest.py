import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.ui.steps.home_page import HomePage
from framework.logger.logger import Logger


@pytest.fixture(scope="session", name="logger")
def start_logger():
    """start logger

    Returns:
        loger: Logger._instance
    """
    logger = Logger.get_logger()
    return logger


@pytest.fixture(scope="session", name="browser_chrome")
def open_browser_chrome():
    """run browser Chrome

    Yields:
        browser: webdriver.Chrome
    """
    options = Options()
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function", name="browser_firefox")
def open_browser_firefox():
    """run browser firefox

    Yields:
        browser: webdriver.Firefox
    """
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function", name="home_page")
def open_home_page(browser_chrome):
    """open home page and check that it opens with correct url

    Args:
        browser_chrome fixture: open_browser_chrome

    Returns:
        app.ui.steps.home_page.HomePage: home_page
    """
    home_page = HomePage(browser_chrome, HomePage.home_page_url)
    home_page.open()
    home_page.should_be_home_page()
    return home_page
