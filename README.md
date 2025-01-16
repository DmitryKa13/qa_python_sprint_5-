# Финальный проект спринта №5 - автоматизация UI тестирования для сервиса Stellar Burgers.
1. Основа для написания автотестов — фреймворк pytest.
2. Команда для запуска — python -m pytest -v. 
3. Список тестов:

		tests/test_account_registration.py::test_registration_valid_input
		tests/test_account_registration.py::test_registration_invalid_password
		tests/test_burger_constructor.py::TestBurgerConstructor::test_open_constructor_from_personal_info_by_constructor_link
		tests/test_burger_constructor.py::TestBurgerConstructor::test_open_constructor_from_personal_info_by_logotype
		tests/test_burger_constructor.py::TestBurgerConstructor::test_check_constructor_select_sauces_tab
		tests/test_burger_constructor.py::TestBurgerConstructor::test_check_constructor_select_buns_tab
		tests/test_burger_constructor.py::TestBurgerConstructor::test_check_constructor_select_fillings_tab
		tests/test_login_page.py::TestLogin::test_check_login_from_main_page
		tests/test_login_page.py::TestLogin::test_check_login_from_personal_account_button
		tests/test_login_page.py::TestLogin::test_check_login_from_forgot_password_form
		tests/test_login_page.py::TestLogin::test_check_login_from_registration_form
		tests/test_personal_account.py::TestPersonalAccount::test_check_go_to_personal_account
		tests/test_personal_account.py::TestPersonalAccount::test_check_exit_from_personal_account

