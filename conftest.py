import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from locators.locators import locators


@pytest.fixture
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.maximize_window()
    browser.get("https://stellarburgers.nomoreparties.site/")

    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*locators.LOGIN_BTN).click()
    driver.find_element(*locators.EMAIL_INPUT_LOGIN_PAGE).send_keys('varcher@example.net')
    driver.find_element(*locators.PASSWORD_INPUT_LOGIN_PAGE).send_keys('142543534')
    driver.find_element(*locators.LOGIN_BUTTON).click()
    return driver
