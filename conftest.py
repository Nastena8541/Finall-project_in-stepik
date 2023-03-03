import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='Chrome',  # или default=None,
        help='Choose browser: Chrome, Firefox, Edge'
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',  # или default=None,
        help='Language'
    )

