from pages.user_account_page import UserAccountPage
from pages.login_page import LoginPage
from data.urls import USER_ACCOUNT, HISTORY_ORDERS, LOGIN_USER

class TestUserAccount:
    def test_go_to_user_account(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        user_acc = UserAccountPage(driver)
        user_acc.click_account()
        user_acc.check_url('/account/profile')

        assert user_acc.get_url() == USER_ACCOUNT

    def test_go_to_history_orders(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        user_acc = UserAccountPage(driver)
        user_acc.click_account()
        user_acc.check_url('/account/profile')

        user_acc.click_history_orders()
        user_acc.check_url('/account/order-history')

        assert user_acc.get_url() == HISTORY_ORDERS

    def test_logout_account(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        user_acc = UserAccountPage(driver)
        user_acc.click_account()
        user_acc.check_url('/account/profile')

        user_acc.click_logout()

        user_acc.check_url('/login')

        assert user_acc.get_url() == LOGIN_USER
