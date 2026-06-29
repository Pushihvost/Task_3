import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators as LL
from locators.main_locators import MainLocators as ML
from data.urls import LOGIN_USER

class MainPage(BasePage):

    @allure.step("Переход на страницу логина")
    def open_login_page(self):
        self.open(LOGIN_USER)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Клик на конструктор")
    def click_constructor(self):
        self.click_element(ML.BURGER_CONSTRUCTOR)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Получить заголовок конструктора")
    def get_header_constructor(self):
        return self.get_text(ML.HEADER_CONSTRUCTOR)

    @allure.step("Клик на ленту заказов")
    def click_lenta_orders(self):
        self.click_element(ML.LENTA_ORDERS)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Получить заголовок ленты заказов")
    def get_header_lenta_order(self):
        return self.get_text(ML.LENTA_ORDERS_HEADER)

    @allure.step("Клик на ингредиент 'Флюоресцентная булка'")
    def click_ingredient(self):
        self.click_element(ML.FLUORESCENT_BUN)

    @allure.step("Получить заголовок деталей ингредиента")
    def get_header_ingredient_details(self):
        return self.get_text(ML.INGREDIENT_DETAILS)

    @allure.step("Закрыть окно деталей ингредиента")
    def close_window_ingredient_details(self):
        self.click_element(ML.CLOSE_INGREDIENT_DETAILS)

    @allure.step("Проверить, что окно деталей ингредиента не отображается")
    def check_not_display_ingredient_details(self):
        return self.is_invisible_element(ML.INGREDIENT_DETAILS)

    @allure.step("Добавить булку в корзину")
    def add_bun_in_busket(self):
        self.drag_and_drop(ML.FLUORESCENT_BUN, ML.BURGER_BUSKET)

    @allure.step("Получить значение счётчика булки")
    def get_counter_bun(self):
        return int(self.get_text(ML.COUNTER_BUN))

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_make_order(self):
        self.click_element(ML.MAKE_ORDER)

    @allure.step("Проверить, что 'Идентификатор заказа' отображается")
    def check_is_id_order_exist(self):
        if self.find_element(ML.ID_ORDER_TEXT):
            return True
        return False

    @allure.step("Закрыть модалку 'Заказ оформлен'")
    def close_window_ordered(self):
        self.js_click(ML.CLOSE_ORDER)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

