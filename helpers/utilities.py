import string
import random
from helpers.data import Data
from helpers.locators import TestLoginLocators, TestBurgerConstructorLocators, TestPersonalAccountLocators, TestRegistrationLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Выполнение входа по кнопке «Войти в аккаунт» на главной
def do_login_from_login_page(driver, name = Data.account_login, password = Data.account_password):
    driver.find_element(*TestLoginLocators.name_field).send_keys(name)
    driver.find_element(*TestLoginLocators.password_field).send_keys(password)
    driver.find_element(*TestLoginLocators.login_button).click()
    personal_account = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.order_button))
    assert personal_account.is_displayed(), "Вход не выполнен."

# Выполнение регистрации по кнопке «Зарегистрироваться» в форме регистрации
def do_registration(driver, name, email, password):
    driver.find_element(*TestRegistrationLocators.name_field).send_keys(name)
    driver.find_element(*TestRegistrationLocators.email_field).send_keys(email)
    driver.find_element(*TestRegistrationLocators.password_field).send_keys(password)
    driver.find_element(*TestRegistrationLocators.registration_button).click()
    login_page = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))
    assert login_page.is_displayed(), "Переход на страницу входа не выполнен."

# Переход в личный кабинет по клику на «Личный кабинет»
def open_personal_account_info(driver):
    driver.find_element(*TestBurgerConstructorLocators.personal_account_button).click()
    profile = WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestPersonalAccountLocators.profile_tab))
    assert profile.is_displayed(), "Личный кабинет не показан."

# Выход из аккаунта по кнопке «Выйти» в личном кабинете.
def exit_personal_account_info(driver):
    driver.find_element(*TestPersonalAccountLocators.exit_button).click()
    entrance = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))
    assert entrance.is_displayed(), "Выход из аккаунта не выполнен."

# Генератор логина
def generate_login():
    login = 'dimaka' + str(random.randint(0000, 9999)) + '@ya.ru'
    return login

# Генератор пароля
def generate_password(length = 6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
