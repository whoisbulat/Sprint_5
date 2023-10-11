from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators

class TestConstructorSection:
    def test_constructor_go_to_buns(self, driver):
        driver.find_element(*locators.CONSTRUCTOR_BTN_SAUCES).click()
        driver.find_element(*locators.CONSTRUCTOR_BTN_BUNS).click()
        text = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                 (locators.CONSTRUCTOR_BTN_ACTIVE))).text
        assert text == 'Булки'



    def test_constructor_go_to_sauces(self, driver):
        driver.find_element(*locators.CONSTRUCTOR_BTN_SAUCES).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                 (locators.CONSTRUCTOR_BTN_ACTIVE))).text
        assert text == 'Соусы'


    def test_constructor_go_to_filling(self, driver):
        driver.find_element(*locators.CONSTRUCTOR_BTN_FILLING).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                 (locators.CONSTRUCTOR_BTN_ACTIVE))).text
        assert text == 'Начинки'