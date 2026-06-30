from pages.user_account_page import UserAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.urls import USER_ACCOUNT, HISTORY_ORDERS, LOGIN_USER, LOGIN_PATH, ACCOUNT_PROFILE_PATH, ACCOUNT_HISTORY_PATH
import allure

class TestUserAccount:

    @allure.title("Тест: переход в личный кабинет")
    @allure.step("Авторизоваться и перейти в личный кабинет")
    def test_go_to_user_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(registered_user)

        user_acc = UserAccountPage(driver)
        main_page.click_account()
        user_acc.check_url(ACCOUNT_PROFILE_PATH)

        assert user_acc.get_url() == USER_ACCOUNT

    @allure.title("Тест: переход в историю заказов")
    @allure.step("Авторизоваться, открыть личный кабинет и перейти в историю заказов")
    def test_go_to_history_orders(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(registered_user)

        user_acc = UserAccountPage(driver)
        main_page.click_account()
        user_acc.check_url(ACCOUNT_PROFILE_PATH)

        user_acc.click_history_orders()
        user_acc.check_url(ACCOUNT_HISTORY_PATH)

        assert user_acc.get_url() == HISTORY_ORDERS

    @allure.title("Тест: выход из личного кабинета")
    @allure.step("Авторизоваться и выйти из личного кабинета")
    def test_logout_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        login_page.login_user(registered_user)

        user_acc = UserAccountPage(driver)
        main_page.click_account()
        user_acc.check_url(ACCOUNT_PROFILE_PATH)

        user_acc.click_logout()

        user_acc.check_url(LOGIN_PATH)

        assert user_acc.get_url() == LOGIN_USER
