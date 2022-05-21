import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.logger.logger import Logger


@pytest.fixture(scope="session")
def logger():
    logger = Logger.get_logger()
    return logger


@pytest.fixture(scope="session")
def open_browser_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(
        options=options, executable_path=ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def open_browser_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(
        options=options, executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
