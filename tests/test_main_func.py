import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

class TestMainFunc:

    @allure.title("Тест: переход в раздел «Конструктор»")
    @allure.step("Открыть страницу и перейти в раздел «Конструктор»")
    def test_go_to_constructor(self, driver):

        main_page = MainPage(driver)

        main_page.open_login_page()
        main_page.click_constructor()

        assert main_page.get_header_constructor() == 'Соберите бургер'

    @allure.title("Тест: переход в раздел «Лента заказов»")
    @allure.step("Открыть раздел «Лента заказов»")
    def test_go_to_lenta_orders(self, driver):

        main_page = MainPage(driver)

        main_page.click_lenta_orders()

        assert main_page.get_header_lenta_order() == 'Лента заказов'

    @allure.title("Тест: открытие окна с деталями ингредиента")
    @allure.step("Открыть модальное окно с деталями ингредиента")
    def test_open_window_details_ingredient(self, driver):

        main_page = MainPage(driver)

        main_page.click_ingredient()
        
        assert main_page.get_header_ingredient_details() == 'Детали ингредиента'

    @allure.title("Тест: закрытие окна с деталями ингредиента")
    @allure.step("Открыть и закрыть модальное окно с деталями ингредиента")
    def test_close_window_details_ingredient(self, driver):

        main_page = MainPage(driver)

        main_page.click_ingredient()
        main_page.close_window_ingredient_details()

        assert main_page.check_not_display_ingredient_details()

    @allure.title("Тест: увеличение счётчика ингредиента после добавления в корзину")
    @allure.step("Добавить ингредиент в корзину и проверить увеличение счётчика")
    def test_add_ingredient_counter_increase(self, driver):

        main_page = MainPage(driver)

        old_counter =  main_page.get_counter_bun()
        main_page.add_bun_in_busket()

        assert main_page.get_counter_bun() == old_counter + 2

    @allure.title("Тест: авторизованный пользователь может оформить заказ")
    @allure.step("Авторизоваться и оформить заказ")
    def test_create_order_authorized_user(self, driver, authorized_user):
        login_page = LoginPage(driver)
        login_page.login_user(authorized_user)

        main_page = MainPage(driver)
        main_page.add_bun_in_busket()
        main_page.click_make_order()

        assert main_page.check_is_id_order_exist()