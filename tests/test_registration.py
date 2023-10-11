from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators
faker = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):
        email = faker.email()
        print(email)
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.REGISTER_BTN).click()
        driver.find_element(*locators.NAME_INPUT).send_keys('тестовый')
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys('142543534')
        driver.find_element(*locators.REGISTER_SUBMIT_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_incorrect_password_error(self, driver):
        email = faker.email()
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.REGISTER_BTN).click()
        driver.find_element(*locators.NAME_INPUT).send_keys('тестовый')
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys('1422')
        driver.find_element(*locators.REGISTER_SUBMIT_BTN).click()
        assert driver.find_element(*locators.PASSWORD_ERROR_MSG)
