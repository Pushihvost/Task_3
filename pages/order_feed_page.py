from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as OFL
import allure

class OrderFeed(BasePage):

    @allure.step("Открыть детали первого заказа")
    def click_first_order(self):
        self.click_element(OFL.FIRST_ORDER)

    @allure.step("Проверить открытие окна с деталями заказа")
    def check_window_order_details_open(self):
        if self.find_element(OFL.ORDER_POPUP_DETAILS):
            return True
        return False
    
    @allure.step("Проверить наличие заказа {order_number} в ленте заказов")
    def check_is_order_by_number_find(self, order_number):
        if self.find_element(OFL.order_by_number(order_number)):
            return True
        return False

    @allure.step("Получить количество заказов за всё время")
    def get_and_return_count_orders_all_time(self):
        return int(self.get_text(OFL.COUNTER_ORDER_ALL_TIME))

    @allure.step("Получить количество заказов за сегодня")
    def get_and_return_count_orders_today(self):
        return int(self.get_text(OFL.COUNTER_ORDER_TODAY))

    @allure.step("Проверить наличие заказа {work_number} в разделе «В работе»")
    def wait_appear_id_in_work(self, work_number):
        if self.find_element(OFL.order_in_work_by_number(work_number.lstrip("#"))):
            return True
        return False
                
