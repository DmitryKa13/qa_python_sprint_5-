import helpers.utilities
from helpers.data import Data


class TestPersonalAccount:

    # Переход в личный кабинет | Проверка переход по клику на «Личный кабинет».
    def test_check_go_to_personal_account(self, driver, login_from_login_page):
        helpers.utilities.open_personal_account_info(driver)
        assert driver.current_url == Data.profile_page_url

    # Выход из аккаунта | Проверка выхода по кнопке «Выйти» в личном кабинете.
    def test_check_exit_from_personal_account(self, driver, open_personal_account_page):
        helpers.utilities.exit_personal_account_info(driver)
        assert driver.current_url == Data.login_page_url
