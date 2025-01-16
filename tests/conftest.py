import helpers.utilities
import pytest
from helpers.data import Data
from helpers.locators import TestMainPageLocators, TestLoginLocators, TestRegistrationLocators, TestForgotPasswordLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Создание драйвера Chrome
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Открытие главной страницы Stellar Burgers
@pytest.fixture
def open_main_page(driver):
    driver.get(Data.MAIN_PAGE_URL)
    assert driver.current_url == Data.MAIN_PAGE_URL

# Открытие страницы авторизации по кнопке «Войти в аккаунт»
@pytest.fixture
def open_login_page_from_main_page(driver, open_main_page):
    driver.find_element(*TestMainPageLocators.enter_to_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))

# Открытие страницы авторизации через кнопку «Личный кабинет»
@pytest.fixture
def open_login_page_from_personal_account_button(driver, open_main_page):
    driver.find_element(*TestMainPageLocators.personal_account_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))

# Открытие страницы регистрации
@pytest.fixture
def open_registration_form_from_login_page(driver, open_login_page_from_main_page):
    driver.find_element(*TestLoginLocators.registration_link).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestRegistrationLocators.registration_label))

# Открытие страницы авторизации через кнопку в форме регистрации
@pytest.fixture
def open_login_page_from_registration_form(driver, open_registration_form_from_login_page):
    driver.find_element(*TestRegistrationLocators.login_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))

# Открытие страницы авторизации через кнопку в форме восстановления пароля
@pytest.fixture
def open_login_page_from_forgot_password_form(driver, open_login_page_from_main_page):
    driver.find_element(*TestLoginLocators.forgot_password_link).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestForgotPasswordLocators.forgot_password_label))
    driver.find_element(*TestForgotPasswordLocators.login_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginLocators.entrance_label))

# Вход с логином и паролем
@pytest.fixture
def login_from_login_page(driver, open_login_page_from_main_page):
    helpers.utilities.do_login_from_login_page(driver)

# Вход с логином и паролем и переход в Личный кабинет
@pytest.fixture
def open_personal_account_page(driver, login_from_login_page):
    helpers.utilities.open_personal_account_info(driver)
