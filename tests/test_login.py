import helpers.utilities


class TestLogin:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_check_login_from_main_page(self, driver, open_login_page_from_main_page):
        helpers.utilities.do_login_from_login_page(driver)

    # Вход через кнопку «Личный кабинет»
    def test_check_login_from_personal_account_button(self, driver, open_login_page_from_personal_account_button):
        helpers.utilities.do_login_from_login_page(driver)

    # Вход через кнопку в форме восстановления пароля
    def test_check_login_from_forgot_password_form(self, driver, open_login_page_from_forgot_password_form):
        helpers.utilities.do_login_from_login_page(driver)

    # Вход через кнопку в форме регистрации
    def test_check_login_from_registration_form(self, driver, open_login_page_from_registration_form):
        helpers.utilities.do_login_from_login_page(driver)
