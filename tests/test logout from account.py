from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators
class TestLogout:
        def test_successful_logout(self, login):
            driver = login
            driver.find_element(*locators.LOGIN_BTN).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (locators.LOGOUT_BTN))).click()
            text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (locators.LOGIN_HEADER))).text
            assert text == 'Вход'




