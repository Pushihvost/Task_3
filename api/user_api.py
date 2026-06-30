from api.base_api import BaseApi
from data.endpoints import (
    REGISTER_USER,
    LOGIN_USER,
    USER_DATA
)
import allure


class UserApi(BaseApi):

    @allure.step("Создать пользователя")
    def create_user(self, payload):
        return self.post(REGISTER_USER, payload)

    @allure.step("Логин пользователя")
    def login_user(self, payload):
        return self.post(LOGIN_USER, payload)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        return self.delete(
            USER_DATA,
            headers={"Authorization": token}
        )
