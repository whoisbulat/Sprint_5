from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestNavigattionPersonalAccount:
        def test_transition_on_page_personal_account(self, login):
            driver = login
            driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
            text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'Профиль')]"))).text
            assert text == 'Профиль'