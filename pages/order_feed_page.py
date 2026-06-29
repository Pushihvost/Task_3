from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as OFL
from selenium.webdriver.common.by import By
import time

class OrderFeed(BasePage):

    def click_first_order(self):
        self.click_element(OFL.FIRST_ORDER)

    def check_window_order_details_open(self):
        if self.find_element(OFL.ORDER_POPUP_DETAILS):
            return True
        return False

    def check_is_order_by_number_find(self, order_number):
        if self.find_element((By.XPATH, f"//p[contains(text(), '{order_number}')]")):
            return True
        return False

    def get_and_return_count_orders_all_time(self):
        return int(self.get_text(OFL.COUNTER_ORDER_ALL_TIME))

    
    def get_and_return_count_orders_today(self):
        return int(self.get_text(OFL.COUNTER_ORDER_TODAY))

    def wait_appear_id_in_work(self, id_order, timeout=5):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                id = self.get_text(OFL.ORDER_IN_WORK)
                if id == id_order.lstrip("#"):
                    return True
            except:
                pass
            time.sleep(0.5)
    
        return False
                
