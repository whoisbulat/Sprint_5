from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators


class TestLoginStellarburger:
    def test_login_by_button_sign_in_on_main_page(self, login):
        driver = login
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (locators.HEADER_TEXT_ON_MAIN ))).text
        assert text == 'Соберите бургер'


    def test_authorization_by_my_account_button(self, driver):
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.EMAIL_INPUT_LOGIN_PAGE).send_keys('varcher@example.net')
        driver.find_element(*locators.PASSWORD_INPUT_LOGIN_PAGE).send_keys('142543534')
        driver.find_element(*locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (locators.HEADER_TEXT_ON_MAIN ))).text
        assert text == 'Соберите бургер'


    def test_authorization_by_button_in_form_registration(self, driver):
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.REGISTRATION_BTN).click()
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.EMAIL_INPUT_LOGIN_PAGE).send_keys('varcher@example.net')
        driver.find_element(*locators.PASSWORD_INPUT_LOGIN_PAGE).send_keys('142543534')
        driver.find_element(*locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (locators.HEADER_TEXT_ON_MAIN ))).text
        assert text == 'Соберите бургер'


    def test_authorization_by_button_in_form_forgot_password(self, driver):
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*locators.SIGN_IN_LINK).click()
        driver.find_element(*locators.EMAIL_INPUT_LOGIN_PAGE).send_keys('varcher@example.net')
        driver.find_element(*locators.PASSWORD_INPUT_LOGIN_PAGE).send_keys('142543534')
        driver.find_element(*locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.HEADER_TEXT_ON_MAIN)).text
        assert text == 'Соберите бургер'