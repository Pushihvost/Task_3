from pages.base_page import BasePage
from locators.login_locators import LoginLocators as LL
from locators.main_locators import MainLocators as ML
from locators.user_account_locators import UserAccountLocators as UAL

class UserAccountPage(BasePage):

    def click_account(self):
        self.click_element(ML.USER_ACCOUNT_LINK)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    def click_history_orders(self):
        self.click_element(UAL.HISTORY_ORDERS)

    def click_logout(self):
        self.click_element(UAL.LOGOUT_ACCOUNT)

    def get_and_return_id_order_in_history(self):
        return self.get_text(UAL.ID_FIRST_ORDER_IN_HISTORY)

    def get_last_order_id(self):
        self.click_account()
        self.check_url("/account/profile")

        self.click_history_orders()
        self.check_url("/account/order-history")

        return self.get_and_return_id_order_in_history()






        