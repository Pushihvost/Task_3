from pages.base_page import BasePage
from data.urls import LOGIN_USER
from locators.login_locators import LoginLocators as LL
import allure

class LoginPage(BasePage):

    @allure.step("Создать пользователя с помощью фикстуры, передать данные на странице логона в ui, Войти")
    def login_user(self, registered_user):

        user = registered_user['user']

        self.open(LOGIN_USER)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)
        self.send_keys_element(LL.EMAIL_INPUT, user['email'])
        self.send_keys_element(LL.PASSWORD_INPUT, user['password'])
        self.click_element(LL.LOGIN_BUTTON)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)

    @allure.step("Нажать на кнопку 'Восстановить пароль'")
    def click_recovery_password_button(self):
        self.click_element(LL.RECOVERY_PASSWORD_LINK)

    @allure.step("Переход на страницу логина с кнопкой 'Восстановить пароль'")
    def open_login_page(self):
        self.open(LOGIN_USER)
        self.wait_overlay_disappear(LL.MODAL_WINDOW)
