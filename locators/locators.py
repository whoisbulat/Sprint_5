from selenium.webdriver.common.by import By

class locators:
    # регистрация
    REGISTER_BTN = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # регистрация кнопка зарегистрироваться
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")  # регистрация поле имя
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]") # регистрация поле электронная почта
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # регистрация поле пароль
    REGISTER_SUBMIT_BTN = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # регистрация кнопка подтвердить регистрацию
    PASSWORD_ERROR_MSG = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # сообщение об ошибке некорректного пароля

    # авторизация
    REGISTRATION_BTN = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # Кнопка «Зарегистрироваться»
    EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='name']") # поле для ввода емайла на странице авторизации
    PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='Пароль']") # поле для ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа на странице авторизации
    HEADER_TEXT_ON_MAIN = (By.XPATH, "//h1[text()='Соберите бургер']") # заголовок на главной странице Соберите бургер
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Кнопка восстановить пароль
    SIGN_IN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]") # Кнопка войти на странице забыли пароль
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(),'Вход')]") # заголовок "Вход"


    # личный кабинет
    LOGOUT_BTN = (By.XPATH, "//button[contains(text(),'Выход')]") # кнопка 'Выход' в личном кабинете

    # хедер
    CONSTRUCTOR_BTN = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # кнопка перехода в 'Конструктор'
    LOGIN_BTN = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # кнопка "личный кабинет" на главной странице
    LOGO_ON_HEADER = (By.XPATH, "(//a [@href = '/'])[2]")  # Логотип  Stellar Burgers


    # главная страница
    BURGER_TITLE_ON_MAIN = (By.XPATH, "//h1[text()='Соберите бургер']") # 'Соберите бургер'
    CONSTRUCTOR_BTN_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")  # раздел Булки
    CONSTRUCTOR_BTN_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]") # раздел Соусы
    CONSTRUCTOR_BTN_FILLING = (By.XPATH, "//span[contains(text(),'Начинки')]") # раздел Начинки
    CONSTRUCTOR_BTN_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


