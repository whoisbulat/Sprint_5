from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import locators

class TestNavigattionPersonalAccount:
        def test_transition_on_page_personal_account(self, login):
            driver = login
            driver.find_element(*locators.LOGIN_BTN).click()
            text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (locators.TEXT_PROFILE_ON_PAGE_USER_ACCOUNT))).text
            assert text == 'Профиль'