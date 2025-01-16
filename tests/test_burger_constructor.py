from helpers.locators import TestBurgerConstructorLocators, TestPersonalAccountLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBurgerConstructor:

    # Переход из личного кабинета в конструктор по клику на "Конструктор"
    def test_open_constructor_from_personal_info_by_constructor_link(self, driver, open_personal_account_page):
        driver.find_element(*TestPersonalAccountLocators.constructor_button).click()
        constructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.order_button))
        assert constructor.is_displayed(), "Переход в конструктор не выполнен"

    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_open_constructor_from_personal_info_by_logotype(self, driver, open_personal_account_page):
        driver.find_element(*TestPersonalAccountLocators.logotype_link).click()
        constructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.order_button))
        assert constructor.is_displayed(), "Переход в конструктор не выполнен"

    # Раздел «Конструктор» | Проверка, что работает переход к разделу «Соусы»
    def test_check_constructor_select_sauces_tab(self, driver, login_from_login_page):
        driver.find_element(*TestBurgerConstructorLocators.sauces_tab).click()
        sauces_label = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.sauces_label))
        assert sauces_label.is_displayed(), "Раздел 'Соусы' не выбран"

    # Раздел «Конструктор» | Проверка, что работает переход к разделу «Булки»
    def test_check_constructor_select_buns_tab(self, driver, login_from_login_page):
        driver.find_element(*TestBurgerConstructorLocators.sauces_tab).click()
        driver.find_element(*TestBurgerConstructorLocators.buns_tab).click()
        buns_label = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.buns_label))
        assert buns_label.is_displayed(), "Раздел 'Булки' не выбран"

    # Раздел «Конструктор» | Проверка, что работает переход к разделу «Начинки»
    def test_check_constructor_select_fillings_tab(self, driver, login_from_login_page):
        driver.find_element(*TestBurgerConstructorLocators.fillings_tab).click()
        fillings_label = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestBurgerConstructorLocators.fillings_label))
        assert fillings_label.is_displayed(), "Раздел 'Начинки' не выбран"
