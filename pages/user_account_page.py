from pages.base_page import BasePage
from locators.user_account_locators import UserAccountLocators as UAL
from data.urls.py import ACCOUNT_PROFILE_PATH, ACCOUNT_HISTORY_PATH
import allure

class UserAccountPage(BasePage):

    @allure.step("Перейти в раздел «История заказов»")
    def click_history_orders(self):
        self.click_element(UAL.HISTORY_ORDERS)

    @allure.step("Нажать кнопку «Выход»")
    def click_logout(self):
        self.click_element(UAL.LOGOUT_ACCOUNT)

    @allure.step("Получить номер последнего заказа из истории")
    def get_and_return_id_order_in_history(self):
        return self.get_text(UAL.ID_FIRST_ORDER_IN_HISTORY)

    @allure.step("Открыть историю заказов и получить номер последнего заказа")
    def get_last_order_id(self):
        self.check_url(ACCOUNT_PROFILE_PATH)

        self.click_history_orders()
        self.check_url(ACCOUNT_HISTORY_PATH)

        return self.get_and_return_id_order_in_history()






        
