import allure
from pages.reset_page import ResetPage
from pages.login_page import LoginPage
from data.urls import FORGOT_PASSWORD, RESET_PASSWORD



class TestResetPass:

    @allure.title("Тест: переход на страницу восстановления пароля")
    @allure.step("Открыть страницу логина и перейти на страницу восстановления пароля")
    def test_click_recovery_password_button_redirect_to_recovery_page(self, driver):
        reset_page = ResetPage(driver)
        login_page = LoginPage(driver)
        
        login_page.open_login_page()       
        login_page.click_recovery_password_button()

        assert reset_page.get_url() == FORGOT_PASSWORD

    @allure.title("Тест: переход на страницу ввода нового пароля после отправки email")
    @allure.step("Ввести email, нажать кнопку «Восстановить» и перейти на страницу сброса пароля")
    def test_email_enter_and_reset_click(self, driver):
        reset_page = ResetPage(driver)

        reset_page.open_forgot_password_page()
        reset_page.fill_email("test@test.ru")
        reset_page.click_recovery_button()
        reset_page.check_url('/reset-password')

        assert reset_page.get_url() == RESET_PASSWORD

    @allure.title("Тест: активация поля пароля при нажатии на кнопку показать/скрыть пароль")
    @allure.step("Перейти на страницу сброса пароля и проверить активацию поля пароля")
    def test_show_password_button_activates_field(self, driver):
        reset_page = ResetPage(driver)

        reset_page.open_forgot_password_page()
        reset_page.fill_email("test@test.ru")
        reset_page.click_recovery_button()
        reset_page.check_url('/reset-password')
        reset_page.click_show_password_button()
        
        assert reset_page.is_password_field_active()


