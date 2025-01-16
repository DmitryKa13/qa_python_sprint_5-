from helpers.locators import TestRegistrationLocators
from helpers.utilities import generate_password, generate_login, do_registration, do_login_from_login_page
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Успешная регистрация
def test_registration_valid_input(driver, open_registration_form_from_login_page):
    login = generate_login()
    password = generate_password()
    do_registration(driver, 'TestUser', login, password)
    do_login_from_login_page(driver, login, password)

# Регистрация с некорректным (5 символом) паролем
def test_registration_invalid_password(driver, open_registration_form_from_login_page):
    driver.find_element(*TestRegistrationLocators.name_field).send_keys('TestUser')
    driver.find_element(*TestRegistrationLocators.email_field).send_keys(generate_login())
    driver.find_element(*TestRegistrationLocators.password_field).send_keys(generate_password(5))
    driver.find_element(*TestRegistrationLocators.registration_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestRegistrationLocators.invalid_password_hint))
