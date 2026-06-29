import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeed
from pages.user_account_page import UserAccountPage

class TestOrderFeed:

    @allure.title("Тест: открытие деталей заказа из ленты заказов")
    @allure.step("Открыть первый заказ из ленты и проверить отображение его деталей")
    def test_click_order_and_open_window_details_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_lenta_orders()

        order_feed = OrderFeed(driver)
        order_feed.click_first_order()
        
        assert order_feed.check_window_order_details_open()

    @allure.title("Тест: созданный заказ отображается в истории и в ленте заказов")
    @allure.step("Создать заказ, открыть историю заказов и убедиться, что заказ присутствует в ленте")
    def test_create_order_go_to_history_go_to_feed_order_find_order(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        main_page = MainPage(driver)
        main_page.add_bun_in_busket()
        main_page.click_make_order()
        main_page.close_window_ordered()

        user_acc = UserAccountPage(driver)

        id_order = user_acc.get_last_order_id()

        main_page.click_lenta_orders()

        order_feed = OrderFeed(driver)
        assert order_feed.check_is_order_by_number_find(id_order)

    @allure.title("Тест: счётчик выполненных заказов за всё время увеличивается после оформления заказа")
    @allure.step("Создать заказ и проверить увеличение общего счётчика выполненных заказов")
    def test_counter_orders_all_time_increase_after_create_order(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        main_page = MainPage(driver)
        main_page.click_lenta_orders()

        order_feed = OrderFeed(driver)
        counter_before_create_order = order_feed.get_and_return_count_orders_all_time()

        main_page.click_constructor()
        main_page.add_bun_in_busket()
        main_page.click_make_order()
        main_page.close_window_ordered()  
        
        #Проверка заказа добавлена, чтобы и заказ нашелся и счётчик успел обновиться
        user_acc = UserAccountPage(driver)

        id_order = user_acc.get_last_order_id()

        main_page.click_lenta_orders()

        order_feed.check_is_order_by_number_find(id_order)
        counter_after_create_order = order_feed.get_and_return_count_orders_all_time()

        assert counter_after_create_order > counter_before_create_order

    @allure.title("Тест: счётчик выполненных заказов за сегодня увеличивается после оформления заказа")
    @allure.step("Создать заказ и проверить увеличение дневного счётчика выполненных заказов")
    def test_counter_orders_today_increase_after_create_order(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        main_page = MainPage(driver)
        main_page.click_lenta_orders()

        order_feed = OrderFeed(driver)
        counter_before_create_order = order_feed.get_and_return_count_orders_today()

        main_page.click_constructor()
        main_page.add_bun_in_busket()
        main_page.click_make_order()
        main_page.close_window_ordered()  
        
        user_acc = UserAccountPage(driver)

        id_order = user_acc.get_last_order_id()

        main_page.click_lenta_orders()

        order_feed.check_is_order_by_number_find(id_order)
        counter_after_create_order = order_feed.get_and_return_count_orders_today()

        assert counter_after_create_order > counter_before_create_order

    @allure.title("Тест: созданный заказ отображается в разделе «В работе»")
    @allure.step("Создать заказ и проверить его появление в списке заказов «В работе»")
    def test_order_in_work(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        main_page = MainPage(driver)
        main_page.add_bun_in_busket()
        main_page.click_make_order()
        main_page.close_window_ordered()

        user_acc = UserAccountPage(driver)

        id_order = user_acc.get_last_order_id()

        main_page.click_lenta_orders()

        order_feed = OrderFeed(driver)
        assert order_feed.wait_appear_id_in_work(id_order)







