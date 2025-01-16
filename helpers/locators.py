from selenium.webdriver.common.by import By


# Главная страница
class TestMainPageLocators:
    # Кнопка 'Войти в аккаунт'
    enter_to_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Гиперссылка 'Личный кабинет'
    personal_account_link = (By.LINK_TEXT, "Личный Кабинет")

# Страница 'Вход'
class TestLoginLocators:
    # Надпись 'Вход' на странице
    entrance_label = (By.XPATH, "//div//h2[text()='Вход']")
    # Поле 'Email'
    name_field = (By.NAME, "name")
    # Поле 'Пароль'
    password_field = (By.NAME, "Пароль")
    # Кнопка 'Войти'
    login_button = (By.XPATH, "//button[text()='Войти']")
    # Гиперссылка 'Зарегистрироваться'
    registration_link = (By.LINK_TEXT, "Зарегистрироваться")
    # Гиперссылка 'Восстановить пароль'
    forgot_password_link = (By.LINK_TEXT, "Восстановить пароль")

# Страница 'Регистрация'
class TestRegistrationLocators:
    # Надпись 'Регистрицая' на странице
    registration_label = (By.XPATH, "//div//h2[text()='Регистрация']")
    # Поле 'Имя'
    name_field = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    # Поле 'Email'
    email_field = (By.XPATH, "//label[text()='Email']/parent::div/input")
    # Поле 'Пароль'
    password_field = (By.NAME, "Пароль")
    # Кнопка 'Зарегистрироваться'
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Гиперссылка 'Войти'
    login_link = (By.LINK_TEXT, "Войти")
    # Некорректный пароль
    invalid_password_hint = (By.CSS_SELECTOR, ".input_status_error")

# Страница 'Восстановление пароля'
class TestForgotPasswordLocators:
    # Надпись 'Восстановление пароля' на странице
    forgot_password_label = (By.XPATH, "//div//h2[text()='Восстановление пароля']")
    # Гиперссылка 'Войти'
    login_link = (By.LINK_TEXT, "Войти")

# Страница 'Конструктор'
class TestBurgerConstructorLocators:
    # Вкладка 'Булки'
    buns_tab = (By.XPATH, "//div[span[text()='Булки']]")
    # Вкладка 'Соусы'
    sauces_tab = (By.XPATH, "//div[span[text()='Соусы']]")
    # Вкладка 'Начинки'
    fillings_tab = (By.XPATH, "//div[span[text()='Начинки']]")
    # Метка 'Булки' в списке
    buns_label = (By.XPATH, "//div//h2[text()='Булки']")
    # Метка 'Соусы' в списке
    sauces_label = (By.XPATH, "//div//h2[text()='Соусы']")
    # Метка 'Начинки' в списке
    fillings_label = (By.XPATH, "//div//h2[text()='Начинки']")
    # Кнопка 'Оформить заказ'
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка 'Личный кабинет'
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")

# Страница 'Личный кабинет'
class TestPersonalAccountLocators:
    # Вкладка 'Профиль'
    profile_tab = (By.XPATH, "//a[@href='/account/profile']")
    # Кнопка 'Выход'
    exit_button = (By.XPATH, "//button[text()='Выход']")
    # Кнопка 'Конструктор'
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип
    logotype_link = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
