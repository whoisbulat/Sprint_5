from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators


class TestConstructorTransitionFromPersonalAccount:
    def test_transition_to_constructor_from_personal_account_by_click_constructor(self, driver):
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.CONSTRUCTOR_BTN).click()
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (locators.BURGER_TITLE_ON_MAIN))).text
        assert text == 'Соберите бургер'



    def test_transition_to_constructor_from_personal_account_by_logo_stellar_burgers(self, driver):
        driver.find_element(*locators.LOGIN_BTN).click()
        driver.find_element(*locators.LOGO_ON_HEADER).click()
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (locators.BURGER_TITLE_ON_MAIN))).text
        assert text == 'Соберите бургер'