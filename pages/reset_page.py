from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators as FPL
from locators.reset_password_locators import ResetPasswordLocators as RPL
from locators.login_locators import LoginLocators as LL
from data.urls import LOGIN_USER, FORGOT_PASSWORD
import allure


class ResetPage(BasePage):

    @allure.step("Переход на страницу логина с кнопкой 'Восстановить пароль'")
    def open_login_page(self):
        self.open(LOGIN_USER)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Нажать на кнопку 'Восстановить пароль'")
    def click_recovery_password_button(self):
        self.click_element(LL.RECOVERY_PASSWORD_LINK)
 
    @allure.step("Переход на страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.open(FORGOT_PASSWORD)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Ввод почты")
    def fill_email(self, email):
        self.click_element(FPL.EMAIL_INPUT)
        self.send_keys_element(FPL.EMAIL_INPUT, email)
    

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_recovery_button(self):
        self.click_element(FPL.RECOVER_BUTTON)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_element(RPL.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        return self.find_element(RPL.PASSWORD_FIELD_ACTIVE)


